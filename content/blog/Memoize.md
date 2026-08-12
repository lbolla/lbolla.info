---
title: Memoize
date: 2008-04-17
tags:
- programming
- python
---
Recently, from a [discussion](http://groups.google.it/group/scipy-user/browse_thread/thread/d1bbbe898d099904/1cb8574c84168c57?hl=it&lnk=gst&q=memoize#1cb8574c84168c57) on the [scipy-user group](http://groups.google.it/group/scipy-user) I discovered a very elegant way to code a function with memory.

Let\'s state the problem. Suppose you need a function that remembers, for each time it has been called, the input parameters and its output. This can be very useful in many different situations:

-   If it is very expensive to evaluate, you can check its memory to see if it has been previously evaluated and, if yes, get its return value without actually calling it.
-   Inside an optimization loop, to remember all the intermediate steps of the optimization.
-   To accumulate data on the behaviour of the function itself.
-   To surprise friends ;-)

The function\'s memory can be as long as the program\'s running time, or it can be \"permanent\" if hard-coded in a file. Starting from [here](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/466320) I\'ve put together a couple of useful classes in python that can be used as decorators.

They are used as follows:

``` python
# function to memoize
def f(x):
    return x**2

# memoized function
memoized_f = memoize(f)

# memoized function on a file
memoized_persistent_f = memoize_persistent(f)
```

Decorators can be used:

``` python
# function to memoize
@memoize # or @memoize_persistent
def f(x):
    return x**2
```

Which is equivalent to: `f = memoize(f)`. You can [download the code here](http://www.box.net/shared/rxf5ul00sc).

Enjoy!
