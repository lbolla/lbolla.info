---
title: org-based lbolla.info
date: 2018-01-04
tags:
- programming
---
[lbolla.info](https://lbolla.info) is now written in [Org](http://orgmode.org/).

I use `org-mode` daily for all sorts of tasks:

-   TODO list
-   Keeping tracks of meetings, events, etc.
-   Note taking
-   Presentations

It was annoying to have to switch to another markdown language for blogging. So, I looked into [org-publish](https://orgmode.org/worg/org-tutorials/org-publish-html-tutorial.html) for a simple, no-frills way to write `.org` files and convert them to `.html`.

My `org-publish-project-alist` now contains these entries:

```lisp
("lbolla.info"
 :components ("lbolla.info-html" "lbolla.info-static" "lbolla.info-cv"))
("lbolla.info-static"
 :base-directory "~/src/lbolla.info/static/"
 :base-extension "png\\|jpg\\|\\|gif\\|gz\\|css"
 :publishing-directory "~/src/lbolla.info/html/"
 :recursive t
 :publishing-function org-publish-attachment)
("lbolla.info-cv"
 :base-directory "~/src/lbolla.info/org/"
 :exclude "\\.*"
 :include ("cv.org")
 :publishing-directory "~/src/lbolla.info/html/"
 :publishing-function org-latex-publish-to-pdf)
("lbolla.info-html"
 :base-directory "~/src/lbolla.info/org/"
 :publishing-directory "~/src/lbolla.info/html/"
 :recursive t
 :section-numbers nil
 :auto-sitemap t
 :sitemap-format-entry lbolla.info/org-publish-sitemap-format-entry
 :sitemap-function lbolla.info/org-publish-sitemap-function
 :sitemap-sort-files anti-chronologically
 :sitemap-style tree
 :sitemap-title "Sitemap"
 :with-toc nil
 :html-doctype "html5"
 :html-head-include-default-style nil
 :html-head-include-scripts nil
 :html-link-home "<ignored>"
 :html-link-up "<ignored>"
 :html-home/up-format "<div id=\"org-div-home-and-up\"><a accesskey=\"h\" href=\"/\">Home</a> | <a accesskey=\"a\" href=\"/articles\">Articles</a> | <a accesskey=\"c\" href=\"/cv\">CV</a> (<a href=\"/cv.pdf\">pdf</a>)</div>"
 :html-preamble lbolla.info/html-preamble
 :html-postamble nil
 :html-head "<link rel=\"stylesheet\" href=\"./css/org.css\" type=\"text/css\">"
 :html-head-extra "<link rel=\"stylesheet\" href=\"./css/extra.css\" type=\"text/css\">"
 :publishing-function org-html-publish-to-html)
```

Style is [this one](http://gongzhitaao.org/orgcss/): some CSS rules made for org-generated HTML files.

Publication is done simply with `rsync`.

The only problem so far is that generating a sitemap is very very slow. It turns out that the problem is with Org not caching certain files properties, used when generating the sitemap: you can [read more here](https://lists.gnu.org/archive/html/emacs-orgmode/2017-12/msg00561.html) if interested. A patch is already available in org\'s repository.
