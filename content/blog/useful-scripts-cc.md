---
categories:
  - "programming"
date: "2012-11-09"
description: "Series about useful scripts"
tags:
  - "rc"
  - "acme"
  - "useful-scripts"
  - "python"
title: "Useful scripts - c+/c-"
---

This is the second post of a [series][1] describing simple scripts that I wrote
to ease my life as a programmer.

They are [available on github][3]: fork & hack at will!

## c+/c-

In this post I'll describe a very simple script, [`c+`][4], and its counterpart
[`c-`][5].

`c+` prepends every line of `stdin` with `#`. `c-` strips `#` from the
beginning of each line of `stdin`. I use these scripts to comment/uncomment
lines in Python scripts when using [`acme`][2].

![c+/c- in acme][7]

Here is the code:

### c+

    #!/usr/bin/env rc

    sed 's/^/#/'

### c-

    #!/usr/bin/env rc

    sed 's/^#//'

 [1]: /blog/tag/useful-scripts/
 [2]: http://acme.cat-v.org/
 [3]: https://github.com/lbolla/cmd
 [4]: https://github.com/lbolla/cmd/blob/master/c%2B
 [5]: https://github.com/lbolla/cmd/blob/master/c-
 [7]: /blog/img/cc_acme.png
