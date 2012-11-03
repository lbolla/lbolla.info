# Haskell and VIM

- title: Haskell and VIM
- author: lbolla
- category: programming
- tags: gist,haskell,vim
- summary: 
- post_id: 319
- date: 2011-10-15 11:13:15
- post_date_gmt: 2011-10-15 10:13:15
- comment_status: open
- post_name: haskell-and-vim
- status: publish
- post_type: post

----------------

I had to tinker quite a bit before finding a decent configuration for vim to edit Haskell files. Here are the packages and config files I use: 

  * [Haskell mode][1]: interaction with [Haddock][2], compiler integration, and other general settings.
  * [Indentation][3]: proper source code indentation.
  * More configs to enforce [good style][4] (no tabs, tabstops, etc.): [gist id=1289349 bump=2]
You can also have them [bundled all together][5].

   [1]: http://projects.haskell.org/haskellmode-vim/
   [2]: http://www.haskell.org/haddock/
   [3]: http://www.vim.org/scripts/script.php?script_id=1968
   [4]: http://urchin.earth.li/~ian/style/haskell.html
   [5]: http://lbolla.info/blog/wp-content/uploads/2011/10/haskell-vim-config.tar.gz