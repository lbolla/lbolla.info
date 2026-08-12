---
title: Die zombie, die!
date: 2014-01-23
tags:
- programming
- python
---
The [`subprocess`](https://docs.python.org/2/library/subprocess.html) module in Python standard library allows you to spanw processes to do some tasks. The parent process should [`wait`](https://docs.python.org/2/library/subprocess.html#subprocess.Popen.wait) on its children processes in order get the return value of the process and [avoid](http://stackoverflow.com/questions/320232/ensuring-subprocesses-are-dead-on-exiting-python-program) [zombies](http://stackoverflow.com/questions/2760652/how-to-kill-or-avoid-zombie-processes-with-subprocess-module).

Sometimes, though, processes are particularly hard to kill and even after a [`wait`](https://docs.python.org/2/library/subprocess.html#subprocess.Popen.wait), a [`terminate`](https://docs.python.org/2/library/subprocess.html#subprocess.Popen.terminate) or a [`kill`](https://docs.python.org/2/library/subprocess.html#subprocess.Popen.kill) they refuse to die: they become [zombies](http://en.wikipedia.org/wiki/Zombie_process).

In theory, Python should take care of reaping zombies for you once the zombie process gets garbage collected. In practice, it does not seem to work reliably and bigger weapons are needed.

Take for example the following script:

<script src="https://gist.github.com/8576490.js?file=zombies.py"></script>

Here I create 3 processes, without holding any references to them, wait for them to finish, and I would expect the GC to kick in and reap them when done. Instead, they are left as zombies until the parent process exits.

Forcing GC does not work either:

<script src="https://gist.github.com/8576490.js?file=zombies_gc.py"></script>

One way is to explicitely `del` them:

<script src="https://gist.github.com/8576490.js?file=zombies_gc_refs.py"></script>

Another way is to explicitly cycle over all the children of the main process and `os.waitpid` on them: this has the effect of removing the zombies from the process table:

<script src="https://gist.github.com/8576490.js?file=zombies_sweep.py"></script>
