---
categories:
  - "programming"
date: "2013-01-22"
tags:
  - "tornado"
  - "futures"
  - "python"
title: "Blocking tasks in Tornado"
---

Every now and then a [new discussion is raised on Tornado's mailling list about what is the best way to execute blocking tasks][3]. It turns out that there are 3 feasible options, in order of increasing complexity:

* _Optimize blocking calls_. Often, a slow DB query, or an overly complicate template are the blocking bottleneck. Rather than complicating the webserver, the first thing to try is to speed them up. This is sufficient 99% of the time.
* _Execute the slow task in a separate thread or process_. This means off-loading the task to a different thread (or process) to the one running the `IOLoop`, which is then free to accept other requests.
* _Use an asynchronous driver/library to run the task_. For example, something like [gevent][4], [motor][5] and the like.

This blog post is about the second option, in particular using Python's [`concurrent.futures`][2] package.

For example, consider this simple web server, with a blocking "SleepHandler" handler:

    import time
    
    import tornado.ioloop
    import tornado.web
    
    
    class MainHandler(tornado.web.RequestHandler):
    
        def get(self):
            self.write("Hello, world %s" % time.time())
    
    
    class SleepHandler(tornado.web.RequestHandler):
    
        def get(self, n):
            time.sleep(float(n))
            self.write("Awake! %s" % time.time())
    
    
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/sleep/(\d+)", SleepHandler),
    ])
    
    
    if __name__ == "__main__":
        application.listen(8888)
        tornado.ioloop.IOLoop.instance().start()

Try to visit `http://localhost:8888/sleep/10` in one tab and `http://localhost:8888/` in another: you'll see that "Hello, world" is not printed in the second tab until the first one has finished, after 10 seconds. Effectively, the first call is blocking the IOLoop, who cannot serve the second tab.

You can make the "SleepHandler" Tornado-friendly by executing it in another thread. Below is a decorator that can be used to "unblock" it: 

    from concurrent.futures import ThreadPoolExecutor
    from functools import partial, wraps
    
    import tornado.ioloop
    import tornado.web
    
    
    EXECUTOR = ThreadPoolExecutor(max_workers=4)
    
    
    def unblock(f):
    
        @tornado.web.asynchronous
        @wraps(f)
        def wrapper(*args, **kwargs):
            self = args[0]

            def callback(future):
                self.write(future.result())
                self.finish()

            EXECUTOR.submit(
                partial(f, *args, **kwargs)
            ).add_done_callback(
                lambda future: tornado.ioloop.IOLoop.instance().add_callback(
                    partial(callback, future)))
    
        return wrapper


    class SleepHandler(tornado.web.RequestHandler):
    
        @unblock
        def get(self, n):
            time.sleep(float(n))
            return "Awake! %s" % time.time()

Very simply, the `unblock` decorator submits the decorated function to the thread pool, which returns a future; a callback is added to this future to return control to the IOLoop, by calling `add_callback`, which eventually will call `self.finish` and conclude the request.

Note that the decorated function must be itself be decorated with `tornado.web.asynchronous`, in order to not call `self.finish` too soon! Moreover, `self.write` is not thread-safe (thanks mrjoes!) therefore it must be called in the main thread with the future's result as parameter.

Full code is below, available on [gist][6].

<script src="https://gist.github.com/4594879.js"></script>

   [1]: http://www.tornadoweb.org/documentation/index.html
   [2]: http://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures
   [3]: https://groups.google.com/d/topic/python-tornado/NVA5sTFIlPo/discussion
   [4]: http://www.gevent.org/
   [5]: http://emptysquare.net/blog/introducing-motor-an-asynchronous-mongodb-driver-for-python-and-tornado/
   [6]: https://gist.github.com/4594879
