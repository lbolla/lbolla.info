---
title: Boundary Value Problem
date: 2008-04-14
---
For you, Python lover, who always needs Matlab functions: boundary value problems are not a problem anymore.

Googling for a [bvp4c](http://www.mathworks.com/access/helpdesk/help/techdoc/index.html?/access/helpdesk/help/techdoc/ref/bvp4c.html&http://www.google.com/cse?cx=002683415331144861350%3Atsq8didf9x0&q=bvp4c&ie=utf-8&oe=utf-8&cof=FORID%3A1&sa=Search) clone, I ended up [here](http://www.elisanet.fi/ptvirtan/software/bvp/index.html):

> This is a Python wrapper for a [modified](http://www.elisanet.fi/ptvirtan/software/bvp/colnew.f.diff) version of the [COLNEW](http://www.netlib.org/ode/colnew.f) boundary value problem solver by U. Ascher and G. Bader. Modifications made include vectorization over mesh points and better compatibility with Python.

There are little differences in the usage, though. I tried to reproduce the examples in [this tutorial](http://www.mathworks.com/matlabcentral/fileexchange/loadFile.do?ref=bvp_tutorial&objectId=3819&objectType=file), to clarify things. You can download the first two examples [here](http://www.box.net/shared/2akb4asoo0).

Enjoy!
