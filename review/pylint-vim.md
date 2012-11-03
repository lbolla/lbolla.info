# pylint.vim

- title: pylint.vim
- author: lbolla
- category: programming
- tags: pylint,python,vim
- summary: 
- post_id: 291
- date: 2011-08-25 10:48:52
- post_date_gmt: 2011-08-25 10:48:52
- comment_status: open
- post_name: pylint-vim
- status: publish
- post_type: post

----------------

vim + python + [pylint][1] is a powerful combination, especially when using this [vim plugin][2]. unfortunately, the script stopped working after a pylint upgrade: [shell] $ pylint --version pylint 0.24.0, astng 0.22.0, common 0.56.0 Python 2.7.2 (default, Jun 29 2011, 11:10:00) [GCC 4.6.1] [/shell] you can download the [fixed version here][3]! if interested, the patch looks like this: [diff] diff pylint.vim.orig pylint.vim 69c69 < CompilerSet makeprg=(echo\ '[%]';\ pylint\ -r\ y\ %) --- > CompilerSet makeprg=(echo\ '[%]';\ pylint\ -r\ y\ --output-format=parseable\ %) 74c74 < CompilerSet efm=%+P[%f],%t:\ %#%l:%m,%Z,%+IYour\ code%m,%Z,%-G%.%# --- > CompilerSet efm=%f:%l:\ [%t]%m,%f:%l:%m [/diff]

   [1]: http://www.logilab.org/857
   [2]: http://www.vim.org/scripts/script.php?script_id=891
   [3]: https://gist.github.com/1170413

## Comments

**[Xavier](#857 "2012-02-09 13:58:20"):** Hello. Are you aware if it stopped working with another Pylint upgrade? I'm using the script for the first time, and I'm unable to get anything beyond "code rate: 0.00, prev: 0.00" (pylint 0.25.1) Thanks in advance for any input. -Xavier

**[Xavier](#858 "2012-02-11 00:07:22"):** Oops! It was my .vimrc's fault, that was also setting efm https://github.com/sontek/dotfiles/blob/master/_vimrc#L284 that I found in http://sontek.net/turning-vim-into-a-modern-python-ide I also found another fork from the unmantained original vim script: http://www.held.org.il/blog/2011/08/pylint-vim-plugin-update-0-24-0-support/ My apologies. And thanks! -Xavier

**[lbolla](#859 "2012-02-13 09:29:03"):** Good!

