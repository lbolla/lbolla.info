# Long running processes manager

- author: lbolla
- category: programming
- tags: futures,python
- summary: Class to manage long running processes in Python, restarting them
  when necessary
- date: 2014-01-17 15:33:00

----------------

If you want to run multiple processes in Python, the nicest way, in my opinion,
is to use [concurrent.futures][1] (there is a [backport][2] for Python 2.x, too).

A problem that came up recently was to manage multiple long running processes,
intended to run forever, from the same Python process. Using something like
[supervisord][3] wouldn't be ideal, because each individual application would
have its own config file and deployment procedure.

Instead, having just one "master" Python process to drive several other
processes doing the job seemed the easiest solution to manage. The only caveat
is that, being the processes managed long running, you want to restart them as
soon as they die.

See below a take to solve the problem using [concurrent.futures][1]. The class
maintain a reference to the running futures and as soon as one finishes, it
checks if it was successful or not. If not, it re-submits. Callbacks `on_error`
and `on_success` can be overwritten to execute some actions on the finished
futures.

<script src="https://gist.github.com/8475101.js?file=process_manager.py"></script>

   [1]: http://docs.python.org/3.4/library/concurrent.futures.html
   [2]: https://pypi.python.org/pypi/futures
   [3]: http://supervisord.org/
