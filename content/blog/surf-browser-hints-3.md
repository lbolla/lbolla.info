# surf browser hints /3

- author: lbolla
- category: programming
- tags: suckless, c
- summary: 
- date: 2010-01-09 20:37:59

----------------

Another couple of hints about [`surf`][1], after [my previous post][2].

Honestly, I stopped using [`surf`][1] after 0.3 release. I think that the authors stripped
out of the code too much sugar that, not being suckless, was nonetheless
useful: a status bar showing the current URI, for example. Now URI editing is
done via `xprop` and [`dmenu`][3], which is great piece of software, but not always
user friendly (it does not have editing capabilities).

Moreover bookmarking is
a pain as it relies on external shell scripts. Or does it not? I realized that
there is no need to use external shell scripts, as they can be "embedded" in C
code. Here is how.

In `config.h` put these lines, right before the definition of `keys[]`:

    #define BM_PICK { .v = (char *[]){ "/bin/sh", "-c",
    "xprop -id $0 -f _SURF_URI 8s -set _SURF_URI `cat ~/.surf/bookmarks | dmenu ||
    exit 0`",
    winid, NULL } }

    #define BM_ADD { .v = (char *[]){ "/bin/sh", "-c",
    "(echo `xprop -id $0 _SURF_URI | cut -d '"' -f 2` && cat ~/.surf/bookmarks) |
    sort -u > ~/.surf/bookmarks_new && mv ~/.surf/bookmarks_new ~/.surf/bookmarks",
    winid, NULL } }

Then inside `keys[]` definition, add:

    { MODKEY, GDK_b, spawn, BM_PICK }, { MODKEY|GDK_SHIFT_MASK,GDK_b, spawn, BM_ADD }

Now, recompile. in your shiny new surf, `CTRL-B` pops-up `dmenu` with the list of
bookmarks and `CTRL-SHIFT-B` adds the current page to the bookmarks (making sure
to remove duplicate entries).

No need for shell scripts!

   [1]: http://surf.suckless.org
   [2]: /blog/2009/08/25/surf-browser-hints-2/
   [3]: http://tools.suckless.org/dmenu
   [4]: http://surf.suckless.org/files/simple_bookmarking_redux
