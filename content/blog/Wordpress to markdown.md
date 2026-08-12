---
title: Wordpress to markdown
date: 2012-11-12
tags:
- programming
- python
---
Recently, I moved away from [Wordpress](http://wordpress.com/). I did it primarily because [Wordpress is so much more than **just** a blogging platform](http://john.onolan.org/ghost/) and what I needed was just a simple way of publishing posts with embedded code, links and images. Moreover, writing blogs using Wordpress\'s web editor is less than ideal...

The biggest problem to solve when moving away from Wordpress is how to not lose all your posts. Luckily, Wordpress allows you to [export all your stuff in XML](http://codex.wordpress.org/Tools_Export_Screen), but you also need a way to import them in whatever other blogging platform you are going to use.

After some research, I decided to choose a [static site generator](http://mickgardner.com/2011/04/27/An-Introduction-To-Static-Site-Generators.html). Out of all the [available alternatives](http://siliconangle.com/blog/2012/03/20/5-minimalist-static-html-blog-generators-to-check-out/), I picked [Felix Felicis](http://liquidluck.readthedocs.org/en/latest/) (aka \"liquidluck\"): it\'s written in Python, very simple to customize and extend, and with some pleasing themes. Other solutions, like [jekyll](https://github.com/mojombo/jekyll), [public-static](http://publicstatic.org/), etc. are way too \"powerful\" (read \"complicated\") for my taste.

Unfortunately, unlike other more popular alternatives, [Felix Felicis](http://liquidluck.readthedocs.org/en/latest/) does not come with an \"importer\" of Wordpress\'s XML file. So, I decided to [fork one of the existing solutions and adapt it to my needs](https://github.com/lbolla/wp2md/tree/liquidluck).

I also forked the [liquid luck\'s default theme](https://github.com/lepture/liquidluck-theme-moment) and [created my own](https://github.com/lbolla/liquidluck-theme-moment).

If you want to do like me, migrate away from Wordpress and use Felix Felicis as your static site generator, do the following:

1.  Export your posts from Wordpress in an XML file
2.  `git clone` my fork of `wp2md` and run it over the XML file
3.  Manually check that all your links and posts have been properly exported: mine needed almost zero editing!
