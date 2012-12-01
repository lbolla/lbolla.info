# surf browser hints

- author: lbolla
- category: programming
- tags: suckless, c
- summary: 
- date: 2009-08-24 18:13:01

----------------

[`surf`][1] is a simple web browser based on [webkit][2]/gtk+, the same web
engine that powers [Google Chrome][3]. Used with [`dwm`][4] and [dmenu][5], it's
a very powerful, yet simple tool.

Here is a patch to apply X geometry hints to
`surf`, so that `surf` windows behave in `dwm.`

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

Another hint is to create a script to feed `surf` with your favorite bookmarks.

Here it is: 

    #!/bin/sh
    exe="surf -u `cat ~/.bookmarks | dmenu ${1+"$@"}`" && exec $exe

Enjoy! 

   [1]: http://surf.suckless.org
   [2]: http://en.wikipedia.org/wiki/Webkit
   [3]: http://www.google.co.uk/chrome
   [4]: http://dwm.suckless.org
   [5]: http://tools.suckless.org/dmenu
