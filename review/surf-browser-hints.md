# surf browser hints

- title: surf browser hints
- author: lbolla
- category: programming
- tags: browser,surf,web,webkit
- summary: 
- post_id: 127
- date: 2009-08-24 18:13:01
- post_date_gmt: 2009-08-24 16:13:01
- comment_status: open
- post_name: surf-browser-hints
- status: publish
- post_type: post

----------------

[surf][1] is a simple webbrowser based on [webkit][2]/gtk+, the same web engine that powers [Google Chrome][3]. used with [dwm][4] and [dmenu][5], it's a very powerfull, yet simple tool. here is a patch to apply X geometry hints to surf, so that surf windows behave in dwm. ` *** surf.c.orig 2009-08-24 16:41:31.000000000 +0100 --- surf.c 2009-08-24 16:35:02.000000000 +0100 *************** *** 372,377 **** --- 372,381 ---- gtk_container_add(GTK_CONTAINER(c->vbox), c->searchbar); gtk_container_add(GTK_CONTAINER(c->vbox), c->urlbar); + /* Hints */ + GdkGeometry hints = { 1, 1 }; + gtk_window_set_geometry_hints(GTK_WINDOW(c->win), NULL, &hints, GDK_HINT_MIN_SIZE); + /* Setup */ gtk_box_set_child_packing(GTK_BOX(c->vbox), c->urlbar, FALSE, FALSE, 0, GTK_PACK_START); gtk_box_set_child_packing(GTK_BOX(c->vbox), c->searchbar, FALSE, FALSE, 0, GTK_PACK_START); ` another hint is to create a script to feed surf with your favorite bookmarks. here it is: ` #!/bin/sh exe="surf -u `cat ~/.bookmarks | dmenu ${1+"$@"}`" && exec $exe ` enjoy! 

   [1]: http://surf.suckless.org
   [2]: http://en.wikipedia.org/wiki/Webkit
   [3]: http://www.google.co.uk/chrome
   [4]: http://dwm.suckless.org
   [5]: http://tools.suckless.org/dmenu

## Comments

**[Emanuelez](#65 "2009-09-07 11:39:05"):** You might want to give uzbl a try :) http://www.uzbl.org/

**[lbolla](#66 "2009-10-04 13:29:43"):** done already ;-) the config file is too long for my tastes!

