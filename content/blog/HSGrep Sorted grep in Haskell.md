---
title: HSGrep Sorted grep in Haskell
date: 2011-11-27
tags:
- programming
- haskell
---
As an exercise to learn [Haskell](http://haskell.org/haskellwiki/Haskell), I wrote a specialized `grep` to work on sorted files. It uses [binary search](http://en.wikipedia.org/wiki/Binary_search_algorithm) to scan a text file and print all the (consecutive) lines that start with a user defined string.

My program is a rewrite of [`sgrep`](http://sourceforge.net/projects/sgrep/) in [Haskell](http://haskell.org/haskellwiki/Haskell): I called it [HSGrep](https://github.com/lbolla/HSGrep). Code is available on [github](https://github.com/lbolla/HSGrep).

Thanks a lot for [all your useful suggestions](http://codereview.stackexchange.com/q/6318/8638)! As soon as possible, I\'ll post some benchmarking [here]({{< relref "blog/HSGrep benchmarking.md" >}}). (EDIT: [benchmarks now available!]({{< relref "blog/HSGrep benchmarking.md" >}}))

After downloading the [source code](https://github.com/lbolla/HSGrep), build install and run it with:

``` shell
$> cabal build
$> cabal install
$> hsgrep <string> <filename>
```
