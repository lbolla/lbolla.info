# surf browser hints /2

- author: lbolla
- category: programming
- tags: suckless, c, X
- summary: 
- date: 2009-08-25 12:45:04

----------------

Following [yesterday's post][1], here is another useful hint about surf's
usage.

The following script lists the available bookmarks (from `~/.bookmarks`
file) and let's you pick one using `dmenu`. If a new link is inserted, it is
added to the list of known bookmarks, so you won't need to type it in full the
next time:

    #!/bin/sh
    bookmarks=~/.bookmarks
    link=`cat $bookmarks | dmenu ${1+"$@"}` || exit 0
    present=`grep $link $bookmarks`
    if [ "$?" -ne "0" ]; then
        echo $link >> $bookmarks
    fi
    surf -u $link

If you don't want to open a new window, just change the last line to set the
`_SURF_URL` X Property of the surf window you want to use (by clicking on it):

    xprop -f _SURF_URL 8t -set _SURF_URL $link `

   [1]: /blog/2009/08/24/surf-browser-hints