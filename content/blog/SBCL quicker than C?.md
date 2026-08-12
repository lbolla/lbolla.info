---
title: SBCL quicker than C?
date: 2010-12-05
tags:
- programming
---
After reading a [nice conversation on comp.lang.lisp](http://groups.google.com/group/comp.lang.lisp/browse_thread/thread/f5a2d25909ce00d2/61aee068b573f89a) I decided to play a little bit with SBCL and [Debian\'s Shootout Benchmarks](http://shootout.alioth.debian.org/).

I considered the [spectral norm benchmark](http://shootout.alioth.debian.org/u32/benchmark.php?test=spectralnorm&lang=sbcl&lang2=gcc) and compared the C and SBCL implementations.

I started re-running the tests without any further optimization and the results were similar to the ones reported with C beating SBCL by a factor of 2. (for the C optimization used, see [here](http://shootout.alioth.debian.org/u32/benchmark.php?test=spectralnorm&lang=gcc)).

Then, I noticed that there was no =(declaim (optimize (speed 3) (safety 0) (space 0)))= in the SBCL file! I\'ve added it and rerun the test. Here are my results:

```
N=500
gcc 0.15u 0.00s 0.17r
sbcl 0.08u 0.02s 0.21r

N=3000
gcc 5.60u 0.00s 5.69r
sbcl 5.18u 0.01s 5.41r

N=5500
gcc 18.81u 0.01s 19.12r
sbcl 17.42u 0.02s 17.76r
```

SBCL implementation is actually faster than C! You can find the code for the tests [here](https://github.com/lbolla/junk/tree/master/shootout/spectralnorm).
