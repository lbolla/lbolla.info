# surf browser hints /3

- title: surf browser hints /3
- author: lbolla
- category: programming
- tags: script,suckless,surf
- summary: 
- post_id: 145
- date: 2010-01-09 20:37:59
- post_date_gmt: 2010-01-09 18:37:59
- comment_status: open
- post_name: surf-browser-hints-3
- status: publish
- post_type: post

----------------

another couple of hints about [surf][1], after [my previous post][2]. honestly, I stopped using [surf][1] after 0.3 release. I think that the authors stripped out of the code too much sugar that, not being suckless, was nonetheless useful: a status bar showing the current URI, for example. now URI editing is done via xprop and [dmenu][3], which is great piece of software, but not always user friendly (it does not have editing capabilities). moreover bookmarking is a pain as it relies on external shell scripts. or does it not? I realized that there is no need to use external shell scripts, as they can be "embedded" in C code. Here is how. in config.h put these lines, right before the definition of keys[]: ` #define BM_PICK { .v = (char *[]){ "/bin/sh", "-c", "xprop -id $0 -f _SURF_URI 8s -set _SURF_URI `cat ~/.surf/bookmarks | dmenu || exit 0`", winid, NULL } } #define BM_ADD { .v = (char *[]){ "/bin/sh", "-c", "(echo `xprop -id $0 _SURF_URI | cut -d '"' -f 2` && cat ~/.surf/bookmarks) | sort -u > ~/.surf/bookmarks_new && mv ~/.surf/bookmarks_new ~/.surf/bookmarks", winid, NULL } } ` then inside keys[] definition, add: ` { MODKEY, GDK_b, spawn, BM_PICK }, { MODKEY|GDK_SHIFT_MASK,GDK_b, spawn, BM_ADD }, ` now, recompile. in your shiny new surf, CTRL-B pops-up dmenu with the list of bookmarks and CTRL-SHIFT-B adds the current page to the bookmarks (making sure to remove duplicate entries). no need for shell scripts!

   [1]: http://surf.suckless.org
   [2]: http://lbolla.wordpress.com/2009/08/25/surf-browser-hints-2/
   [3]: http://tools.suckless.org/dmenu

## Comments

**[Andrew](#72 "2010-01-11 09:04:07"):** Hey Lorenzo - I put your config.h setup on the suckless wiki, if you want to check it out[1]. Cheers, man! [1] http://surf.suckless.org/files/simple_bookmarking_redux

