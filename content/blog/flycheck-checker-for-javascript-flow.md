---
categories:
  - "programming"
date: "2014-11-19"
description: "Definition of a flyckeck checker for Flow"
tags:
  - "emacs"
  - "javascript"
  - "flow"
title: "Flycheck checker for Flow"
---

[Yesterday][1] Facebook open sourced [Flow][1], a static type checker for Javascript.
If you use [Emacs][3], you can use [Flycheck][4] to check your .js files on the fly using Flow.

Here is the checker definition I use:

<script src="https://gist.github.com/lbolla/476a030ff2fe06445918.js"></script>

I prefer to use Flow *after* [gjslint][5], so I define the following, too:

    (flycheck-add-next-checker 'javascript-gjslint 'javascript-flow)

Enjoy!

   [1]: https://code.prod.facebook.com/posts/1505962329687926/flow-a-new-static-type-checker-for-javascript/
   [2]: http://flowtype.org/
   [3]: http://www.gnu.org/software/emacs/
   [4]: http://flycheck.readthedocs.org/en/latest/
   [5]: https://developers.google.com/closure/utilities/docs/linter_howto
