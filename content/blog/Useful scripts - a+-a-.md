---
title: Useful scripts - a+-a-
date: 2012-11-02
tags:
- programming
- python
---
This is the first post of a series describing simple scripts that I wrote to ease my life as a programmer.

They are implemented in various languages (`python`, `bash`, `go`) and thought to be used in `Linux`. Some of them are \"general purpose\", while others are specifically designed to interface other tools I use (for example, [`acme`](http://acme.cat-v.org/).)

All of them tend to have the following properties:

-   Input from `stdin`, output to `stdout`, errors to `stderr`
-   Return zero on success, non-zero on failure
-   Do one thing only
-   Not too much customizable

These properties allow the scripts to remain very simple, be composable and easy to remember.

They are [available on github](https://github.com/lbolla/cmd): fork & hack at will!

## a+/a-

In this post I\'ll describe a very simple script, [`a+`](https://github.com/lbolla/cmd/blob/master/a%2B), and its counterpart [`a-`](https://github.com/lbolla/cmd/blob/master/a-). They are the first I wrote when I started using [`acme`](http://acme.cat-v.org/).

`a+` indents every line of `stdin` by 4 spaces. `a-` \"de-indents\" it by the same amount. The amount of spaces (4) is fixed (to resist the temptation to change it), and indentation is done with [spaces and not tabs](http://www.python.org/dev/peps/pep-0008/#tabs-or-spaces).

The code is trivial: it uses [`sed`](http://swtch.com/plan9port/man/man1/sed.html) and [`rc`](http://swtch.com/plan9port/man/man1/rc.html), the [Plan9\'s shell ported to \*nix](http://swtch.com/plan9port/) (although, in this case, any shell would do.) Here it is:

### a+

``` shell
# !/usr/bin/env rc  

sed 's/^/ /'  
```

### a-

``` shell
# !/usr/bin/env rc  

sed 's/^ //'  
```
