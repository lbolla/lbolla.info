# vim and Python comments

- author: lbolla
- category: programming
- tags: python, vim
- summary: 
- date: 2009-08-12 17:56:15

----------------

I'm currently undergoing a profound revision (read "cleanup") of my `.vimrc` and
I recently had to choose a decent plug-in to comment python code.

The best so far is [EnhancedCommentify][1]. It's highly configurable, powerful
and it supports a different number of languages (not only python).

The only one thing that wasn't easy to setup if the behaviour described
[here][2]: being able to comment a block, respecting the indent, in both visual
and normal mode.

A clean solution, without the need to define any function is to stick these
lines into your `.vimrc`:

    let g:EnhCommentifyPretty='Yes'
    let g:EnhCommentifyRespectIndent='Yes'
    let g:EnhCommentifyUserBindings="Yes"
    let g:EnhCommentifyUseBlockIndent='Yes'

    vmap ,c (Plug)VisualComment
    vmap ,d (Plug)VisualDeComment
    vmap ,g (Plug)VisualTraditional
    vmap ,f (Plug)VisualFirstLine
    nmap ,c (Plug)Comment
    nmap ,d (Plug)DeComment
    nmap ,g (Plug)Traditional
    nmap ,f (Plug)FirstLine

(but remember to change "(" to "<" and ")" to ">" -- Wordpress is strict about "<" and ">"...)

Enjoy!

   [1]: http://www.vim.org/scripts/script.php?script_id=23http://www.vim.org/scripts/script.php?script_id=23
   [2]: http://chistera.yi.org/~adeodato/blog/entries/2008/03/02/vim_enhanced_commentify_UseBlockIndent_with_nmap.html
