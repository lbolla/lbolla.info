---
title: Haskell and VIM
date: 2011-10-15
tags:
- programming
- haskell
---
I had to tinker quite a bit before finding a decent configuration for vim to edit Haskell files. Here are the packages and config files I use:

-   [Haskell mode](http://projects.haskell.org/haskellmode-vim/): interaction with [Haddock](http://www.haskell.org/haddock/), compiler integration, and other general settings.
-   [Indentation](http://www.vim.org/scripts/script.php?script_id=1968): proper source code indentation.
-   More configs to enforce [good style](http://urchin.earth.li/~ian/style/haskell.html) (no tabs, tabstops, etc.):

<script src="https://gist.github.com/1289349.js"> </script>
You can also have them [bundled all together](./assets/haskell-vim-config.tar.gz).
