# Boundary Value Problem

- author: lbolla
- category: programming
- tags: python, matlab, numerical
- summary: Boundary Value Problem using numpy
- date: 2008-04-14 20:04:20

----------------

For you, Python lover, who always needs Matlab functions: boundary value
problems are not a problem anymore.

Googling for a [bvp4c][1] clone, I ended up [here][2]: 

> This is a Python wrapper for a [modified][3] version of the [COLNEW][4]
> boundary value problem solver by U. Ascher and G. Bader. Modifications made
> include vectorization over mesh points and better compatibility with Python.

There are little differences in the usage, though. I tried to reproduce the
examples in [this tutorial][5], to clarify things. You can download the first
two examples [here][6].

Enjoy!

   [1]: http://www.mathworks.com/access/helpdesk/help/techdoc/index.html?/access/helpdesk/help/techdoc/ref/bvp4c.html&http://www.google.com/cse?cx=002683415331144861350%3Atsq8didf9x0&q=bvp4c&ie=utf-8&oe=utf-8&cof=FORID%3A1&sa=Search (bvp4c)
   [2]: http://www.elisanet.fi/ptvirtan/software/bvp/index.html (BVP)
   [3]: http://www.elisanet.fi/ptvirtan/software/bvp/colnew.f.diff
   [4]: http://www.netlib.org/ode/colnew.f
   [5]: http://www.mathworks.com/matlabcentral/fileexchange/loadFile.do?ref=bvp_tutorial&objectId=3819&objectType=file (bvp_tutorial)
   [6]: http://www.box.net/shared/2akb4asoo0 (bvp_tutorial)
