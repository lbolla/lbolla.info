# numerical computing: matlab vs python+numpy+weave

- title: numerical computing: matlab vs python+numpy+weave
- author: lbolla
- category: programming
- tags: 
- summary: 
- post_id: 32
- date: 2007-04-11 12:06:57
- post_date_gmt: 2007-04-11 10:06:57
- comment_status: open
- post_name: numerical-computing-matlab-vs-pythonnumpyweave
- status: publish
- post_type: post

----------------

recently, I've discovered the power of python for numerical computing. being a slave of matlab for many years, I've decided to give python (and it's numerical module numpy) a try, comparing its numerical crounching capabilities versus matlab's. the tests are heavily insipired by [Prabhu Ramachandran][1]. I've only added matlab to complete his comparisons. Here is a short description of the test, taken from [here][1]: _The example we will consider is a very simple (read, trivial) case of solving the 2D Laplace equation using an iterative finite difference scheme (four point averaging, Gauss-Seidel or Gauss-Jordan). The formal specification of the problem is as follows. We are required to solve for some unknown function u(x,y) such that nabla^2 u = 0 with a boundary condition specified. For convenience the domain of interest is considered to be a rectangle and the boundary values at the sides of this rectangle are given._ all the tests have been run on a Pentium IV Xeon 2GHz, with 1Gb of RAM. here is the matlab script I used [laplace.m][2] (it's a doc file: sorry for that, but I'm only allowed to upload docs and images on this blog). ![time spent by different solvers][3] matlab and numpy have pretty much the same performances. any form of optimization on python code does better than matlab. only the simple python (without numpy) is slower than matlab (note the logarithmic y scale to fit also the "slow" algorithm). ![speed factor with respect to matlab][4] blitz is roughly twice as fast as matlab. inline, fastinline, fortran and pyrex only differ appreciably for small grids: for 500x500 grids they are around 10x faster than matlab. here is some other digits, not included in the graphs: 

  * numpy with psyco runs 5% faster than numpy alone;
  * weave and psyco (blitz, inline and fastinline) fails with following polite error: _local variables of functions run by Psyco cannot be accessed in any way, sorry;_
  * octave runs twice as slow as numpy and matlab.
pretty amazing, if you think that optimizing python, most of the time, is really trivial. moreover, python is free and easily parallelizable with [MPI][5] (I'll show some performances in a future post). tests have been run also on an SGI Altix with Itanium2 processors, on a single CPU. the graphs are reported in the following thumbnails. ![time spent by different solvers][6]![speed factor with respect to matlab][7]

   [1]: http://www.scipy.org/PerformancePython (performance python)
   [2]: http://lbolla.info/blog/wp-content/uploads/2007/04/laplacem.doc (laplace.m)
   [3]: http://lbolla.info/blog/wp-content/uploads/2007/04/time.png
   [4]: http://lbolla.info/blog/wp-content/uploads/2007/04/factor.png
   [5]: http://mpi4py.scipy.org/
   [6]: http://lbolla.info/blog/wp-content/uploads/2007/04/pico_time.png
   [7]: http://lbolla.info/blog/wp-content/uploads/2007/04/pico_factor.png

## Comments

**[lbolla](#13 "2007-04-11 13:45:52"):** thanks to David Joyner for correcting a typo in the post!

**[Michael Lerner](#14 "2007-04-11 18:32:52"):** What happens if you use psyco under the same conditions as blitz?

**[lbolla](#15 "2007-04-18 11:35:23"):** psyco used with weave gives a polite error: "local variables of functions run by Psyco cannot be accessed in any way, sorry." I guess this should be fixed, somehow, but I don't know if it worths the time: numpy+psyco runs just a 5% faster than numpy alone.

**[lorenzo](#16 "2007-09-07 17:05:53"):** other benchmarks specifically on linear algebra can be found here. https://www.osc.edu/blogs/index.php/sip?blog=7&p=37&page=1&more=1&c=1&tb=1&pb=1&disp=single

**[Maximus](#17 "2007-12-20 08:00:11"):** I would like to see a continuation of the topic

**[Rob Steele](#19 "2008-03-06 19:28:05"):** Been there done that. Try R (http://www.r-project.org/). I've never been more productive.

**[Casey](#20 "2008-03-06 22:03:21"):** Ever tried Scilab?

**[Adolph](#21 "2008-03-12 17:36:11"):** I would like to see times for grid sizes 600 to 900?

**[Memming](#22 "2008-07-29 14:54:11"):** What was the version of MATLAB? Did it have JIT compiler on?

**[lbolla](#23 "2008-07-29 15:41:58"):** I used Matlab 6.5, iirc. No JIT compiler.

**[itsrsu](#25 "2009-10-10 10:48:08"):** [ Mathematics of Linear Algebra ][1]

   [1]: http://linearalgebra21.blogspot.com

**[isabel](#26 "2010-02-24 02:54:14"):** hi i have laplace.py, but when i run it it has error i want to know how can i do? or if you can say me how did you install the program, i hace python 2.6 for ubuntu

**[Kitty](#27 "2010-05-28 08:17:22"):** numerical computing: matlab vs python+numpy+weave ? lorenzo bolla’s blogguy@gigemail.net

**[Carlton](#28 "2010-06-02 08:57:26"):** numerical computing: matlab vs python+numpy+weave ? lorenzo bolla’s blog guy@gigemail.net

