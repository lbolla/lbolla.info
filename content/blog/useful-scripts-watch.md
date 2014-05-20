---
categories:
  - "programming"
date: "2012-11-30"
description: "Series about useful scripts"
tags:
  - "acme"
  - "useful-scripts"
  - "python"
title: "Useful scripts - Watch"
---

This is the fifth post of a [series][1] describing simple scripts that I wrote
to ease my life as a programmer.

They are [available on github][3]: fork & hack at will!

[`Watch`][4] reacts to changes in a directory executing a command provided by the
user. It can be used, for example, to monitor a directory and run some
unittests as soon as files in it change. This is exactly how I am using `Watch`
in [`acme`][2].

![Watch in acme][5]

`Watch` is based on the [`pyinotify`][6] library, a very slim, one file library
that I included [my repo][3] for simplicity. Basically, `pyinotify` relies on
`inotify`, an event-driven notifier merged in the Linux kernel since version
2.6.13: given a directory to watch, it raises events that users can process
defining handlers in the `ProcessEvent` class.

One note is that `Watch` refuses to run its command more often that once every
3 seconds. This is to avoid that multiple events raised on the same directory
too quickly queue up too many processes.

Here is the code:

    #!/usr/bin/env python

    # Watch for modified files in localdir (.) and react.
    # ./Watch <cmd>
    # i.e.: ./Watch flake8 .

    from pylib.pyinotify import WatchManager, EventsCodes, ProcessEvent, Notifier
    from subprocess import call
    import sys
    import time


    class ProcessManager(ProcessEvent):

        LAST_TIME = None

        def __init__(self, cmds):
            super(ProcessEvent, self).__init__()
            self.cmds = cmds

        def is_too_soon(self):
            return self.LAST_TIME and time.time() - self.LAST_TIME < 3

        def process_IN_CLOSE_WRITE(self, event):
            # For some reason, this event is triggered twice
            if not self.is_too_soon():
                call(self.cmds)
                self.LAST_TIME = time.time()


    def main():

        dir = '.'
        cmds = sys.argv[1:]

        wm = WatchManager()

        mask = EventsCodes.ALL_FLAGS['IN_CLOSE_WRITE']

        notifier = Notifier(wm, ProcessManager(cmds))
        wm.add_watch(dir, mask, rec=True)

        while True:
            try:
                notifier.process_events()
                if notifier.check_events():
                    notifier.read_events()
            except KeyboardInterrupt:
                notifier.stop()
                break


    if __name__ == '__main__':
        main()


 [1]: /blog/tag/useful-scripts/
 [2]: http://acme.cat-v.org/
 [3]: https://github.com/lbolla/cmd
 [4]: https://github.com/lbolla/cmd/blob/master/Watch
 [5]: /blog/img/watch_acme.png
 [6]: https://github.com/seb-m/pyinotify
