# Asynchronous programming with Tornado

- author: lbolla
- category: programming
- tags: tornado,web,asynchronous
- summary: Tutorial about asynchronous web programming with Tornado
- date: 2012-10-03 12:33:49

----------------

Asynchronous programming can be tricky for beginners, therefore I think it's
useful to iron some basic concepts to avoid common pitfalls. For an explanation
about generic asynchronous programming, I recommend you one of the [many][1]
[resources][2] [online][3]. I will focus solely on asynchronous programming in
[Tornado][4].

From Tornado's homepage: 

> FriendFeed's web server is a relatively simple, non-blocking web server
> written in Python. The FriendFeed application is written using a web
> framework that looks a bit like web.py or Google's webapp, but with
> additional tools and optimizations to take advantage of the non-blocking web
> server and tools. Tornado is an open source version of this web server and
> some of the tools we use most often at FriendFeed. The framework is distinct
> from most mainstream web server frameworks (and certainly most Python
> frameworks) because it is non-blocking and reasonably fast. Because it is
> non-blocking and uses epoll or kqueue, it can handle thousands of
> simultaneous standing connections, which means the framework is ideal for
> real-time web services. We built the web server specifically to handle
> FriendFeed's real-time features every active user of FriendFeed maintains an
> open connection to the FriendFeed servers. (For more information on scaling
> servers to support thousands of clients, see The C10K problem.)

The first step as a beginner is to figure out if you _really_ need to go
asynchronous. Asynchronous programming is more complicated that synchronous
programming, because, as someone described, it does not fit human brain nicely.

You should use asynchronous programming when your application needs to monitor
some resources and react to changes in their state. For example, a web server
sitting idle until a request arrives through a socket is an ideal candidate. Or
an application that has to execute tasks periodically or delay their execution
after some time. The alternative is to use multiple threads (or processes) to
control multiple tasks and this model becomes quickly complicated.

The second step is to figure out if you _can_ go asynchronous. Unfortunately in
Tornado, not all the tasks can be executed asynchronously.

Tornado is single threaded (in its common usage, although in supports multiple
threads in advanced configurations), therefore any "blocking" task will block
the whole server.  This means that a blocking task will not allow the framework
to pick the next task waiting to be processed. The selection of tasks is done
by the [`IOLoop`][5], which, as everything else, runs in the only available
thread.

For example, this is a _wrong_ way of using `IOLoop`:

<script src="https://gist.github.com/3826189.js?file=async_generic.py"></script>

Note that `blocking_call` is called correctly, but, being
blocking (`time.sleep` blocks!), it will prevent the execution of the following
task (the second call to the same function). Only when the first call will end,
the second will be called by `IOLoop`. Therefore, the output in console is
sequential ("sleeping", "awake!", "sleeping", "awake!").

Compare the same
"algorithm", but using an "asynchronous version" of `time.sleep`, i.e.
`add_timeout`:

<script src="https://gist.github.com/3826189.js?file=async_sleep_1.py"></script>

In this case, the first
task will be called, it will print "sleeping" and then it will ask `IOLoop` to
schedule the execution of the rest of the routine after 1 second. `IOLoop`,
having the control again, will fire the second call the function, which will
print "sleeping" again and return control to `IOLoop`. After 1 second `IOLoop`
will carry on where he left with the first function and "awake" will be
printed. Finally, the second "awake" will be printed, too. So, the sequence of
prints will be: "sleeping", "sleeping", "awake!", "awake!". The two function
calls have been executed concurrently ([not in parallel][6], though!).

So, I hear you asking, "how do I create functions that can be executed
asynchronously"? In Tornado, every function that has a "callback" argument can
be used with `gen.engine.Task`. _Beware though_: being able to use `Task` does
not make the execution asynchronous! There is no magic going on: the function
is simply scheduled to execution, executed and whatever is passed to `callback`
will become the return value of `Task`. See below:

<script src="https://gist.github.com/3826189.js?file=async_generic.py"></script>

Most beginners expect to be able to just write: `Task(my_func)`, and
automagically execute `my_func` asynchronously. This is not how Tornado works.
This is how [Go][7] works! And this is my last remark:

> In a function that is going to be used "asynchronously", only asynchronous
> libraries should be used.

By this, I mean that blocking calls like `time.sleep` or
`urllib2.urlopen` or `db.query` will need to be substituted by their equivalent
asynchronous version. For example, `IOLoop.add_timeout` instead of
`time.sleep`, `AsyncHTTPClient.fetch` instead of `urllib2.urlopen` etc. For DB
queries, the situation is more complicated and specific asynchronous drivers to
talk to the DB are needed. For example: [Motor][8] for MongoDB. 

   [1]: http://en.wikipedia.org/wiki/Asynchrony
   [2]: http://www.cs.brown.edu/courses/cs196-5/f12/handouts/async.pdf
   [3]: http://krondo.com/?page_id=1327
   [4]: http://www.tornadoweb.org/documentation/index.html
   [5]: http://www.tornadoweb.org/documentation/ioloop.html?highlight=ioloop#tornado.ioloop.IOLoop
   [6]: http://stackoverflow.com/questions/1897993/difference-between-concurrent-programming-and-parallel-programming
   [7]: http://golang.org/
   [8]: http://blog.mongodb.org/post/30927719826/motor-asynchronous-driver-for-mongodb-and-python

## Comments

**[abdelouahab](#919 "2012-10-03 19:27:41"):** here is another good link to learn, it's a slide explaining the non-blocking in a good-simple way: http://fr.slideshare.net/simon/evented-io-based-web-servers-explained-using-bunnies

**[abdelouahab](#916 "2012-10-03 16:06:04"):** hi thank you, really interresting for us as beginner! by the way, as you said about the libraries, i've tried to use the amazom api library, and because it's blocking then, i always get the error saying the it needs a callback! so here is the asynchronous library for amazon, it's the Boto but asynchronous: https://github.com/yyuu/botornado and this one for facebook: https://github.com/pauloalem/tornado-facebook-sdk

**[lbolla](#917 "2012-10-03 16:20:14"):** @abdelouahab: Thanks for the links, Aliane!

**[abdelouahab](#918 "2012-10-03 19:23:32"):** you're welcome, thank you for "you" for helping us, non-blocking is a real head ache, and espetially for Python users, the problem of GIL will make the solution of using event-handler the best choice! making the apache-way is not a good idea, since making a new thread is valuable for the server (sorry if i dont understand well, this is what i got for now as a beginner) ;)
