---
title: Useful scripts - c+-c-
date: 2012-11-09
tags:
- programming
- python
---
This is the second post of a series describing simple scripts that I wrote to ease my life as a programmer.

They are [available on github](https://github.com/lbolla/cmd): fork & hack at will!

## c+/c-

In this post I\'ll describe a very simple script, [`c+`](https://github.com/lbolla/cmd/blob/master/c%2B), and its counterpart [`c-`](https://github.com/lbolla/cmd/blob/master/c-).

`c+` prepends every line of `stdin` with `#`. `c-` strips `#` from the beginning of each line of `stdin`. I use these scripts to comment/uncomment lines in Python scripts when using [`acme`](http://acme.cat-v.org/).

![c+/c- in acme](/img/cc_acme.png)

Here is the code:

### c+

``` shell
#!/usr/bin/env rc

sed 's/^/#/'
```

### c-

``` shell
#!/usr/bin/env rc

sed 's/^#//'
```
