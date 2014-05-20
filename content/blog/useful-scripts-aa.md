---
categories:
  - "programming"
date: "2012-11-02"
description: "Series about useful scripts"
tags:
  - "rc"
  - "acme"
  - "useful-scripts"
title: "Useful scripts - a+/a-"
---

This is the first post of a [series][1] describing simple scripts that I wrote
to ease my life as a programmer.

They are implemented in various languages (`python`, `bash`, `go`) and thought
to be used in `Linux`. Some of them are "general purpose", while others are
specifically designed to interface other tools I use (for example,
[`acme`][2].)

All of them tend to have the following properties:

*   Input from `stdin`, output to `stdout`, errors to `stderr`
*   Return zero on success, non-zero on failure
*   Do one thing only
*   Not too much customizable

These properties allow the scripts to remain very simple, be composable and
easy to remember.

They are [available on github][3]: fork & hack at will!

## a+/a-

In this post I'll describe a very simple script, [`a+`][4], and its counterpart
[`a-`][5]. They are the first I wrote when I started using [`acme`][2].

`a+` indents every line of `stdin` by 4 spaces. `a-` "de-indents" it by the
same amount. The amount of spaces (4) is fixed (to resist the temptation to
change it), and indentation is done with [spaces and not tabs][6].

The code is trivial: it uses [`sed`][7] and [`rc`][8], the [Plan9's shell
ported to *nix][9] (although, in this case, any shell would do.) Here it is:

### a+

    # !/usr/bin/env rc  

    sed 's/^/ /'  

### a-

    # !/usr/bin/env rc  

    sed 's/^ //'  

 [1]: /blog/tag/useful-scripts/
 [2]: http://acme.cat-v.org/
 [3]: https://github.com/lbolla/cmd
 [4]: https://github.com/lbolla/cmd/blob/master/a%2B
 [5]: https://github.com/lbolla/cmd/blob/master/a-
 [6]: http://www.python.org/dev/peps/pep-0008/#tabs-or-spaces
 [7]: http://swtch.com/plan9port/man/man1/sed.html
 [8]: http://swtch.com/plan9port/man/man1/rc.html
 [9]: http://swtch.com/plan9port/
