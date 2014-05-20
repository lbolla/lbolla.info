---
categories:
  - "programming"
date: "2008-04-17"
description: "None"
tags:
  - "python"
title: "Memoize"
---

Recently, from a [discussion][1] on the [scipy-user group][2] I discovered a
very elegant way to code a function with memory.

Let's state the problem.
Suppose you need a function that remembers, for each time it has been called,
the input parameters and its output. This can be very useful in many different
situations: 

  * If it is very expensive to evaluate, you can check its memory to see if it
    has been previously evaluated and, if yes, get its return value without
    actually calling it.
  * Inside an optimization loop, to remember all the intermediate steps of the
    optimization.
  * To accumulate data on the behaviour of the function itself.
  * To surprise friends ;-)

The function's memory can be as long as the program's running time, or it can
be "permanent" if hard-coded in a file. Starting from [here][3] I've put
together a couple of useful classes in python that can be used as decorators.

They are used as follows:
    
    # function to memoize
    def f(x):
        return x**2
    
    # memoized function
    memoized_f = memoize(f)
    
    # memoized function on a file
    memoized_persistent_f = memoize_persistent(f)

Decorators can be used: 
    
    # function to memoize
    @memoize # or @memoize_persistent
    def f(x):
        return x**2

Which is equivalent to: `f = memoize(f)`. You can [download the code here][4].

Enjoy!

   [1]: http://groups.google.it/group/scipy-user/browse_thread/thread/d1bbbe898d099904/1cb8574c84168c57?hl=it&lnk=gst&q=memoize#1cb8574c84168c57 (discussion)
   [2]: http://groups.google.it/group/scipy-user (scipy-user group)
   [3]: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/466320 (python recipe)
   [4]: http://www.box.net/shared/rxf5ul00sc (memoize.py)
