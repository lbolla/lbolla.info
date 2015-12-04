---
categories:
  - "programming"
date: "2015-11-21"
description: "Python3 sucks"
tags:
  - "python"
title: "Python3 sucks"
---

Slower.

Python2:

  In [1]: x = range(1000)

  In [2]: def f(i):
    ...:     return i + 1
    ...: 

  In [3]: timeit map(f, x)
  The slowest run took 5.26 times longer than the fastest. This could mean that an intermediate result is being cached 
  10000 loops, best of 3: 80.3 µs per loop

  In [4]: timeit [f(i) for i in x]
  The slowest run took 7.01 times longer than the fastest. This could mean that an intermediate result is being cached 
  10000 loops, best of 3: 82.9 µs per loop

  In [5]: timeit {i: i+1 for i in x}
  The slowest run took 7.57 times longer than the fastest. This could mean that an intermediate result is being cached 
  10000 loops, best of 3: 45.2 µs per loop

  In [6]: timeit set(x)
  The slowest run took 5.66 times longer than the fastest. This could mean that an intermediate result is being cached 
  100000 loops, best of 3: 18.9 µs per loop

  # Larger list

  In [7]: y = range(1000000)

  In [9]: timeit map(f, y)
  10 loops, best of 3: 91.5 ms per loop

  # Allocation

  In [10]: timeit range(1000000)
  100 loops, best of 3: 15.3 ms per loop

  # Text

  In [26]: text = ''.join(random.choice(string.letters) for _ in xrange(1000000))

  In [27]: timeit text.count('a')
  The slowest run took 4.19 times longer than the fastest. This could mean that an intermediate result is being cached 
  1000 loops, best of 3: 823 µs per loop

Python3:

  In [1]: x = range(1000)

  In [2]: def f(i):
    ...:     return i + 1
    ...: 

  In [3]: timeit map(f, x)  # just creates an iterator
  10000000 loops, best of 3: 184 ns per loop

  In [4]: timeit list(map(f, x))
  10000 loops, best of 3: 119 µs per loop

  In [5]: timeit [f(i) for i in x]
  10000 loops, best of 3: 121 µs per loop

  In [6]: timeit {i: i+1 for i in x}
  10000 loops, best of 3: 84.4 µs per loop

  In [7]: timeit set(x)
  10000 loops, best of 3: 32.9 µs per loop

  # Larger list
  
  In [8]: y = list(range(1000000))

  In [10]: timeit list(map(f, y))
  10 loops, best of 3: 122 ms per loop

  # Allocation

  In [11]: timeit list(range(1000000))
  10 loops, best of 3: 26 ms per loop

  # Text seems faster

  In [18]: text = ''.join(random.choice(string.ascii_letters) for _ in range(1000000))

  In [19]: timeit text.count('a')
  1000 loops, best of 3: 555 µs per loop
