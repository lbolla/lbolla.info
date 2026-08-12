---
title: Migrating away from wordpress.com
date: 2011-04-11
tags:
- javascript
---
Today I decided to migrate my blog from [wordpress.com](http://lbolla.wordpress.com) to [my own domain](https://lbolla.info/blog).

I did it for many reasons:

-   To be able to [add plugins](http://en.forums.wordpress.com/topic/adding-plugins?replies=8)
-   To be able to [add javascript](http://wordpress.org/support/topic/adding-javascript-to-page) to individual pages
-   To run a [customized theme](http://63222hljwcjlds6no5lczchgsg.hop.clickbank.net/)
-   And all the other reasons listed [here](http://en.support.wordpress.com/com-vs-org/)

I did not want to loose the popularity and the ranking of my original address, accumulated over the years.

Here are the steps I had to follow (if the following steps make no sense to you, [this guide](http://a07086nbyhov3xdnzplolg3tdz.hop.clickbank.net/) might help you):

-   Setup a new empty Wordpress blog at [lbolla.info/blog](https://lbolla.info/blog)
-   Exported the whole old blog as XML file (better called `WordPress eXtended     RSS` or `WXR`): simply log into the admin interface of the old blog and click `Tools > Export`
-   Imported the `WXR` file into the new empty blog by clicking `Tools >     Import` in the admin interface
-   Activate the `Site Redirect` upgrade in the old blog by clicking on `Upgrades` in the left-hand menu of the admin interface and paying a whopping 12\$/year. Here is the description of this service:

> Do you want to move away from WordPress.com to your own self-hosted WordPress installation without losing SEO ranking and breaking links? Have you recently changed your blog address and need to move traffic to the new address? This upgrade redirects your wordpress.com blog to your new blog by performing permanent (301) redirects for all of your content.

All the procedure took no more than 15 minutes. Brilliant.
