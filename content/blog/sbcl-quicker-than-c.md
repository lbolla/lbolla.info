# SBCL quicker than C?

- author: lbolla
- category: programming
- tags: lisp, c, benchmark
- summary: 
- date: 2010-12-05 17:21:02

----------------

After reading a [nice conversation on comp.lang.lisp][1] I decided to play a
little bit with SBCL and [Debian's Shootout Benchmarks][2].

I considered the [spectral norm benchmark][3] and compared the C and SBCL
implementations.

I started re-running the tests without any further optimization and the results
were similar to the ones reported with C beating SBCL by a factor of 2. (for
the C optimization used, see [here][4]).

Then, I noticed that there was no `(declaim (optimize (speed 3) (safety 0)
(space 0)))` in the SBCL file! I've added it and rerun the test. Here are my
results: 

    N=500
    gcc 0.15u 0.00s 0.17r
    sbcl 0.08u 0.02s 0.21r

    N=3000
    gcc 5.60u 0.00s 5.69r
    sbcl 5.18u 0.01s 5.41r

    N=5500
    gcc 18.81u 0.01s 19.12r
    sbcl 17.42u 0.02s 17.76r

SBCL implementation is actually faster than C! You can find the code for the tests [here][5].

   [1]: http://groups.google.com/group/comp.lang.lisp/browse_thread/thread/f5a2d25909ce00d2/61aee068b573f89a (comp.lang.lisp)
   [2]: http://shootout.alioth.debian.org/
   [3]: http://shootout.alioth.debian.org/u32/benchmark.php?test=spectralnorm&lang=sbcl&lang2=gcc
   [4]: http://shootout.alioth.debian.org/u32/benchmark.php?test=spectralnorm&lang=gcc
   [5]: https://github.com/lbolla/junk/tree/master/shootout/spectralnorm (github)

## Comments

**[Anon](#75 "2011-02-08 10:40:22"):** Did you consider submitting your benchmark to shootout?

**[lbolla](#76 "2011-02-08 11:19:53"):** Actually, I did: [spectralnorm][1], [fasta][2] and [pidigits][3].

   [1]: http://shootout.alioth.debian.org/u32/benchmark.php?test=spectralnorm&lang=sbcl&lang2=gcc
   [2]: http://shootout.alioth.debian.org/u32/benchmark.php?test=fasta&lang=sbcl
   [3]: http://shootout.alioth.debian.org/u32/benchmark.php?test=pidigits&lang=sbcl

**[lbolla](#77 "2011-02-08 14:10:03"):** This post triggered a nice discussion, with further analysis, on [Reddit][1].

   [1]: //www.reddit.com/r/lisp/comments/fhcd1/sbcl_quicker_than_c/

**[Robert](#78 "2011-02-08 15:23:21"):** I believe you are shooting yourself in the foot. You should not use -O3 with -Os. You should only use -O3.

**[lbolla](#80 "2011-02-08 16:20:31"):** I've just re-run the C benchmark without -Os (only -O3) but the results are the same.

**[Zach](#81 "2011-02-08 16:42:44"):** C rules.

**[Mateus Caruccio](#82 "2011-02-08 17:58:28"):** Are you considering libc load time? Try strace both process to see how many libs, and it's sizes, each link to.

**[Isaac Gouy](#83 "2011-02-08 18:27:56"):** benchmarks game N CPU Elapsed 5,500 11.14 2.80 spectral-norm C GNU gcc #4 5,500 15.25 3.97 Lorenzo Bolla 2010-12-06 Lisp SBCL #2 http://shootout.alioth.debian.org/u64q/benchmark.php?test=spectralnorm&lang=all

**[lbolla](#84 "2011-02-08 19:23:32"):** The numbers shown on the post are for the benchmark run on my box. In fact, after seeing the results "locally", I submitted the code to the shootout, getting the numbers you (Isaac) correctly show. So, different numbers on different boxes, which is not at all unexpected.

**[Isaac Gouy](#85 "2011-02-08 19:47:11"):** Do you get similar measurements when time isn't a makefile action?

**[lbolla](#86 "2011-02-09 11:55:40"):** yes, same results. why would they be different?

**[Isaac Gouy](#87 "2011-02-10 20:23:02"):** Why would the results be any different on your box? You haven't provided basic information that would allow readers to understand what's the same about the way you made your measurements and what's different about the way you made your measurements. You haven't provided basic information about "your box" or the language tools on "your box".

