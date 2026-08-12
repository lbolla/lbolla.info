---
title: Trivial terminal speed benchmark
date: 2010-04-29
tags:
- programming
---
Today, while playing with [st](http://st.suckless.org), I tried a very simple benchmark. Here it is:

``` shell
$> time seq -f 'teeeeeeeeeeeeeeeeeeeeeeeeeeeeeest %g' 999999
```

Here are the results:

``` shell
xterm: 0m28.508s
rxvt: 0m8.568s
st: 0m12.082s
```

All the terminals shared the same fonts, but [xterm](http://invisible-island.net/xterm/) and [rxvt](http://sourceforge.net/projects/rxvt/) had `saveLines=1024` set for scrolling purposes, feature that [st](http://st.suckless.org) lacks.

Being [st](http://st.suckless.org) at such an early stage of development, I think this is a good result.
