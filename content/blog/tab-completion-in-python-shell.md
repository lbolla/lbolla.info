# Tab completion in Python shell

- author: lbolla
- category: programming
- tags: python
- summary: 
- date: 2008-06-25 11:52:39

----------------

Recently [I saw with this little piece of code][1] to give the standard python shell tab completion capabilities:

    # setup tab completion in python shell
    import rlcompleter
    import readline
    readline.parse_and_bind("tab: complete")

Obviously, you can use the environmental variable `PYTHONSTART` to execute this few lines anytime you start your python shell.

Enjoy!

   [1]: http://groups.google.com/group/comp.lang.python/browse_thread/thread/b1f19db3f69cd8ce#

## Comments

**[h4p0](#50 "2009-12-27 01:57:05"):** I noticed that with CTRL+tab I can get the same result as "double-tab" to get completion. Is there a way to have the normal Tabulator with TAB and the completion with CTRL+TAB?

**[Mark](#51 "2010-01-04 10:17:17"):** You could use ipython too which does this job for you and provides a hoddy of other stuff besides.

