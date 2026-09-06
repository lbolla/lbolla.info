---
title: HSGrep benchmarking
date: 2011-11-30
tags:
- programming
- haskell
---
Few days ago, [I rewrote `sgrep` in Haskell]({{< relref "blog/HSGrep Sorted grep in Haskell.md" >}}). I was curious to know how it compares to [`grep`](http://en.wikipedia.org/wiki/Grep.org) in term of execution speed. In particular, I was interested to verify that `hsgrep` scales as `O(log n)`, instead of `O(n)`, with `n` being the size of the file analyzed.

First of all, in order to have similar performance to `grep`, I had to convert my original program to use [Haskell\'s bytestrings](http://hackage.haskell.org/packages/archive/bytestring/latest/doc/html/Data-ByteString.html). [You can find the code here](https://github.com/lbolla/HSGrep/tree/bytestring). Testing files are generated with [this script](https://github.com/lbolla/HSGrep/blob/bytestring/data/gendata.hs).

Here are the results obtained. `grep` is still faster for smallish files (I haven\'t spent too much time tweaking `hsgrep`), but `hsgrep` scales much better and it wins for files larger than few megabytes!

![HSGrep benchmark](/img/bench1.png)
