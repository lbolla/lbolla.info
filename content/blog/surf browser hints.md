---
title: surf browser hints
date: 2009-08-24
tags:
- programming
---
[`surf`](http://surf.suckless.org) is a simple web browser based on [webkit](http://en.wikipedia.org/wiki/Webkit)/gtk+, the same web engine that powers [Google Chrome](http://www.google.co.uk/chrome). Used with [`dwm`](http://dwm.suckless.org) and [dmenu](http://tools.suckless.org/dmenu), it\'s a very powerful, yet simple tool.

Here is a patch to apply X geometry hints to `surf`, so that `surf` windows behave in `dwm.`

```c
*** surf.c.orig 2009-08-24 16:41:31.000000000 +0100
--- surf.c  2009-08-24 16:35:02.000000000 +0100
***************
*** 372,377 ****
--- 372,381 ----
gtk_container_add(GTK_CONTAINER(c->vbox), c->searchbar);
gtk_container_add(GTK_CONTAINER(c->vbox), c->urlbar);

+ /* Hints */
+ GdkGeometry hints = { 1, 1 };
+ gtk_window_set_geometry_hints(GTK_WINDOW(c->win), NULL, &hints,
  GDK_HINT_MIN_SIZE);
+
/* Setup */
gtk_box_set_child_packing(GTK_BOX(c->vbox), c->urlbar, FALSE, FALSE, 0,
GTK_PACK_START);
gtk_box_set_child_packing(GTK_BOX(c->vbox), c->searchbar, FALSE, FALSE, 0,
GTK_PACK_START);
```

Another hint is to create a script to feed `surf` with your favorite bookmarks.

Here it is:

```sh
#!/bin/sh
exe="surf -u `cat ~/.bookmarks | dmenu ${1+"$@"}`" && exec $exe
```

Enjoy!
