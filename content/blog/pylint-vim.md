---
categories:
  - "programming"
date: "2011-08-25"
description: "None"
tags:
  - "python"
  - "vim"
title: "pylint.vim"
aliases:
  - /blog/2011/08/25/pylint.vim
---

`vim` + Python + [`pylint`][1] is a powerful combination, especially when using this [`vim` plugin][2]. Unfortunately, the script stopped working after a `pylint` upgrade:

    $ pylint --version
    pylint 0.24.0,
    astng 0.22.0, common 0.56.0
    Python 2.7.2 (default, Jun 29 2011, 11:10:00)
    [GCC 4.6.1]

You can download the [fixed version here][3]!

If interested, the patch looks like this:

    diff pylint.vim.orig pylint.vim
    69c69
    < CompilerSet makeprg=(echo\ '[%]';\ pylint\ -r\ y\ %)
    ---
    > CompilerSet makeprg=(echo\ '[%]';\ pylint\ -r\ y\ --output-format=parseable\
    > %)
    74c74
    < CompilerSet efm=%+P[%f],%t:\ %#%l:%m,%Z,%+IYour\ code%m,%Z,%-G%.%#
    ---
    > CompilerSet efm=%f:%l:\ [%t]%m,%f:%l:%m

   [1]: http://www.logilab.org/857
   [2]: http://www.vim.org/scripts/script.php?script_id=891
   [3]: https://gist.github.com/1170413
