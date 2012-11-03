# memoize

- title: memoize
- author: lbolla
- category: programming
- tags: python memoize decorator
- summary: 
- post_id: 64
- date: 2008-04-17 14:51:48
- post_date_gmt: 2008-04-17 12:51:48
- comment_status: open
- post_name: memoize
- status: publish
- post_type: post

----------------

recently, from a [discussion][1] on the [scipy-user group][2] I discovered a very elegant way to code a function with memory. let's state the problem. suppose you need a function that remembers, for each time it has been called, the input parameters and its output. this can be very useful in many different situations: 

  * if it is very expensive to evaluate, you can check its memory to see if it has been previously evaluated and, if yes, get its return value without actually calling it.
  * inside an optimization loop, to remember all the intermediate steps of the optimization.
  * to accumulate data on the behaviour of the function itself.
  * to surprise friends ;-)
the function's memory can be as long as the program's running time, or it can be 'permament' if hard-coded in a file. starting from [here][3] I've put together a couple of useful classes in python that can be used as decorators. they are use as follow: 
    
    # function to memoize
    def f(x):
    return x**2
    
    # memoized function
    memoized_f = memoize(f)
    
    # memoized function on a file
    memoized_persistent_f = memoize_persistent(f)

decorators can be used: 
    
    # function to memoize
    @memoize # or @memoize_persistent
    def f(x):
    return x**2

which is equivalent to: `f = memoize(f)`. you can [download the code here][4]. enjoy!

   [1]: http://groups.google.it/group/scipy-user/browse_thread/thread/d1bbbe898d099904/1cb8574c84168c57?hl=it&lnk=gst&q=memoize#1cb8574c84168c57 (discussion)
   [2]: http://groups.google.it/group/scipy-user (scipy-user group)
   [3]: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/466320 (python recipe)
   [4]: http://www.box.net/shared/rxf5ul00sc (memoize.py)