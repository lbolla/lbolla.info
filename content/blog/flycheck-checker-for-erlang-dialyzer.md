---
categories:
  - "programming"
date: "2015-05-09"
description: "Definition of a flyckeck checker for Erlang's dialyzer"
tags:
  - "emacs"
  - "erlang"
  - "dialyzer"
title: "Flycheck checker for Erlang dialyzer"
---

Emacs Erlang mode misses the definition of a [flycheck][1] checker using [dialyzer][2].
Just add these lines to your `.emacs` to enable it:

<script src="https://gist.github.com/lbolla/c989096bbc0ba31bb834.js"></script>

I prefer to use it *after* the normal Erlang checker, so I define the following, too:

	  (flycheck-add-next-checker 'erlang 'erlang-dialyzer)

Enjoy!

   [1]: http://flycheck.readthedocs.org/en/latest/
   [2]: http://www.erlang.org/doc/man/dialyzer.html
