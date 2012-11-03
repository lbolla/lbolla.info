# migrating away from wordpress.com

- title: migrating away from wordpress.com
- author: lbolla
- category: tech
- tags: migration,redirect,wordpress.com
- summary: 
- post_id: 251
- date: 2011-04-11 14:36:00
- post_date_gmt: 2011-04-11 14:36:00
- comment_status: open
- post_name: migrating-away-from-wordpress-com
- status: publish
- post_type: post

----------------

today I decided to migrate my blog from [wordpress.com][1] to [my own domain][2].

I did it for many reasons:

  * to be able to [add plugins][3]
  * to be able to [add javascript][4] to individual pages
  * to run a [customized theme][5]
  * and all the other reasons listed [here][6]

I did not want to loose the popularity and the ranking of my original address, accumulated over the years.

here are the steps I had to follow (if the following steps make no sense to you, [this guide][7] might help you):

  * setup a new empty wordpress blog at [lbolla.info/blog][2]
  * exported the whole old blog as XML file (better called `WordPress eXtended RSS` or `WXR`): simply log into the admin interface of the old blog and click `Tools > Export`
  * imported the `WXR` file into the new empty blog by clicking `Tools > Import` in the admin interface
  * activate the `Site Redirect` upgrade in the old blog by clicking on `Upgrades` in the left-hand menu of the admin interface and paying a whopping 12$/year. Here is the description of this service: 

> Do you want to move away from WordPress.com to your own self-hosted WordPress installation without losing SEO ranking and breaking links? Have you recently changed your blog address and need to move traffic to the new address? This upgrade redirects your wordpress.com blog to your new blog by performing permanent (301) redirects for all of your content.

all the procedure took no more than 15 minutes. brilliant.

   [1]: http://lbolla.wordpress.com
   [2]: http://lbolla.info/blog
   [3]: http://en.forums.wordpress.com/topic/adding-plugins?replies=8
   [4]: http://wordpress.org/support/topic/adding-javascript-to-page
   [5]: http://63222hljwcjlds6no5lczchgsg.hop.clickbank.net/
   [6]: http://en.support.wordpress.com/com-vs-org/
   [7]: http://a07086nbyhov3xdnzplolg3tdz.hop.clickbank.net/