---
categories:
  - "programming"
date: "2008-06-25"
tags:
  - "python"
title: "Tab completion in Python shell"
---

Recently [I saw with this little piece of code][1] to give the standard python shell tab completion capabilities:

    # setup tab completion in python shell
    import rlcompleter
    import readline
    readline.parse_and_bind("tab: complete")

Obviously, you can use the environmental variable `PYTHONSTART` to execute this few lines anytime you start your python shell.

Enjoy!

   [1]: http://groups.google.com/group/comp.lang.python/browse_thread/thread/b1f19db3f69cd8ce#
