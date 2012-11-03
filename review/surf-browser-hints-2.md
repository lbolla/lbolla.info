# surf browser hints /2

- title: surf browser hints /2
- author: lbolla
- category: programming
- tags: browser,dmenu,surf,webkit
- summary: 
- post_id: 128
- date: 2009-08-25 12:45:04
- post_date_gmt: 2009-08-25 10:45:04
- comment_status: open
- post_name: surf-browser-hints-2
- status: publish
- post_type: post

----------------

following [yesterday's post][1], here is another useful hint about surf's usage. the following script lists the available bookmarks (from ~/.bookmarks file) and let's you pick one using dmenu. if a new link is inserted, it is added to the list of known bookmarks, so you won't need to type it in full the next time: ` #!/bin/sh bookmarks=~/.bookmarks link=`cat $bookmarks | dmenu ${1+"$@"}` || exit 0 present=`grep $link $bookmarks` if [ "$?" -ne "0" ]; then echo $link >> $bookmarks fi surf -u $link ` if you don't want to open a new window, just change the last line to set the _SURF_URL X Property of the surf window you want to use (by clicking on it): ` xprop -f _SURF_URL 8t -set _SURF_URL $link `

   [1]: http://lbolla.wordpress.com/2009/08/24/surf-browser-hints/