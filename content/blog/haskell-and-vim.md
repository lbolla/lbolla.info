---
categories:
  - "programming"
date: "2011-10-15"
description: "None"
tags:
  - "haskell"
  - "vim"
title: "Haskell and VIM"
---

I had to tinker quite a bit before finding a decent configuration for vim to
edit Haskell files. Here are the packages and config files I use: 

  * [Haskell mode][1]: interaction with [Haddock][2], compiler integration, and
    other general settings.
  * [Indentation][3]: proper source code indentation.
  * More configs to enforce [good style][4] (no tabs, tabstops, etc.):

<script src="https://gist.github.com/1289349.js"> </script>

You can also have them [bundled all together][5].

   [1]: http://projects.haskell.org/haskellmode-vim/
   [2]: http://www.haskell.org/haddock/
   [3]: http://www.vim.org/scripts/script.php?script_id=1968
   [4]: http://urchin.earth.li/~ian/style/haskell.html
   [5]: /blog/assets/haskell-vim-config.tar.gz
