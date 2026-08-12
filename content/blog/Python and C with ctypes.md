---
title: Python and C with ctypes
date: 2013-08-28
tags:
- programming
- python
- javascript
---
Calling C code from Python is very simple using [ctypes](https://docs.python.org/2/library/ctypes.html). Here is a very simple example to get you started and to serve as a reminder for me!

Let\'s say you have this C file, defining 3 functions:

-   `foo` which prints something to `stdout`;
-   `bar` which returns and `int`;
-   `baz` which takes a parameter and returns a value.

<script src="https://gist.github.com/lbolla/6363780.js?file=go.c"></script>
First, you want to compile this C file into a shared object. Here is a `Makefile` to do just this: simple type `make all` and you\'re done.

<script src="https://gist.github.com/lbolla/6363780.js?file=Makefile"></script>
Finally, you can call these C functions from Python using [ctypes](https://docs.python.org/2/library/ctypes.html):

<script src="https://gist.github.com/lbolla/6363780.js?file=go.py"></script>
Obviously, there is much more to it and things get more complicated soon, but, as you can see, for simple tasks like this using [ctypes](https://docs.python.org/2/library/ctypes.html) is pretty straitforward.
