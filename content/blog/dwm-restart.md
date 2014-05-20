---
categories:
  - "programming"
date: "2010-01-08"
tags:
  - "dwm"
  - "script"
title: "dwm restart"
---

[`dwm`][1] is a wonderful window manager for X: it's small, fast and stable.

The
only thing I missed, until today, was the possibility to restart it without
losing my X session (i.e. all the open windows, etc.). Restarting `dwm` is
something you might need to do often, as it does not have config files: changes
are done by recompiling the sources.

The trick is to execute `dwm` in background
and sleep forever! Take a look at the last two lines of my `.xinitrc`:

    dwm & sleeper

where `sleeper` looks like this:

    #!/bin/sh
    while `/bin/true`; do
        sleep 1000
    done

Now, if you kill `dwm` (usually with `ALT-SHIFT-q`) the windows (and X) will
still be alive and you can type `dwm&` in any xterm to get `dwm` up and running
again. If you really want to quit X, you need to kill the sleeper. 

   [1]: http://dwm.suckless.org/

