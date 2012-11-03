# dwm restart

- title: dwm restart
- author: lbolla
- category: programming
- tags: dwm,script
- summary: 
- post_id: 143
- date: 2010-01-08 19:14:05
- post_date_gmt: 2010-01-08 17:14:05
- comment_status: open
- post_name: dwm-restart
- status: publish
- post_type: post

----------------

[dwm][1] is a wonderful window manager for X: it's small, fast and stable. the only thing I missed, until today, was the possibility to restart it without losing my X session (i.e. all the open windows, etc.). restarting dwm is something you might need to do often, as it does not have config files: changes are done by recompiling the sources. the trick is to execute dwm in background and sleep forever! take a look at the last two lines of my .xinitrc: ` --- dwm & sleeper --- ` where `sleeper` looks like this: ` --- #!/bin/sh while `/bin/true`; do sleep 1000 done --- ` now, if you kill dwm (usually with ALT-SHIFT-q) the windows (and X) will still be alive and you can type `dwm&` in any xterm to get dwm up and running again. if you really want to quit X, you need to kill the sleeper. 

   [1]: http://dwm.suckless.org/

## Comments

**[Stonebot](#68 "2010-01-28 22:58:43"):** When I try this i go to load dwm and it loads for 1 second then back to the login manager...

**[Neotericpiguy](#69 "2010-03-02 01:39:45"):** while true; do dwm 2> ~/.dwm.log ; done When you kill dwm it will restart right back up. Useful if you update config.h and sudo make install a new binary.

**[meillo](#70 "2010-10-14 21:25:20"):** Instead of `/bin/true` use : . That puts less load onto the machine, is easier to type, and if you know the idiom it's easier to read too. while :; do whatever done

**[Mark](#71 "2010-10-15 09:16:56"):** Thanks, didn't know about the :

