---
categories:
  - "programming"
date: "2012-11-12"
description: "How I decided to drop Wordpress and use markdown"
tags:
  - "markdown"
  - "python"
  - "wordpress"
title: "Wordpress to markdown"
---

Recently, I moved away from [Wordpress][1]. I did it primarily because
[Wordpress is so much more than **just** a blogging platform][4] and
what I needed was just a simple way of publishing posts with embedded
code, links and images. Moreover, writing blogs using Wordpress's web
editor is less than ideal...

The biggest problem to solve when moving away from Wordpress is how to
not lose all your posts. Luckily, Wordpress allows you to [export all
your stuff in XML][2], but you also need a way to import them in
whatever other blogging platform you are going to use.

After some research, I decided to choose a [static site generator][3].
Out of all the [available alternatives][9], I picked [Felix
Felicis][6] (aka "liquidluck"): it's written in Python, very simple to
customize and extend, and with some pleasing themes. Other solutions,
like [jekyll][8], [public-static][7], etc. are way too "powerful"
(read "complicated") for my taste.

Unfortunately, unlike other more popular alternatives, [Felix
Felicis][6] does not come with an "importer" of Wordpress's XML file.
So, I decided to [fork one of the existing solutions and adapt it to
my needs][5].

I also forked the [liquid luck's default theme][10] and [created my
own][11].

If you want to do like me, migrate away from Wordpress and use Felix
Felicis as your static site generator, do the following:

1. Export your posts from Wordpress in an XML file
2. `git clone` my fork of `wp2md` and run it over the XML file
3. Manually check that all your links and posts have been properly
   exported: mine needed almost zero editing!

   [1]: http://wordpress.com/
   [2]: http://codex.wordpress.org/Tools_Export_Screen
   [3]: http://mickgardner.com/2011/04/27/An-Introduction-To-Static-Site-Generators.html
   [4]: http://john.onolan.org/ghost/
   [5]: https://github.com/lbolla/wp2md/tree/liquidluck
   [6]: http://liquidluck.readthedocs.org/en/latest/
   [7]: http://publicstatic.org/
   [8]: https://github.com/mojombo/jekyll
   [9]: http://siliconangle.com/blog/2012/03/20/5-minimalist-static-html-blog-generators-to-check-out/
   [10]: https://github.com/lepture/liquidluck-theme-moment
   [11]: https://github.com/lbolla/liquidluck-theme-moment
