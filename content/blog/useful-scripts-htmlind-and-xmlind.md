---
categories:
  - "programming"
date: "2012-11-23"
description: "Useful scripts to indent HTML and XML files"
tags:
  - "useful-scripts"
  - "python"
  - "acme"
title: "Useful scripts - htmlind and xmlind"
aliases:
  - /blog/2012/11/23/useful-scripts---htmlind-and-xmlind
---

This is the forth post of a [series][1] describing simple scripts that
I wrote to ease my life as a programmer.

In this post I'll describe 2 simple scripts to indent nicely `HTML`
and `XML` files. I use them primarily with [`acme`][2], to pipe
selected text and get back nicely formatted output.

Code is available here: [`htmlind`][3] and [`xmlind`][4]. Both programs are written in Python and make use of specialized libraries freely available online. In particular, `xmlind` uses [`xml.dom.minidom`][6], included in Python's standard library, and `htmlind` uses a modified version of [`BeautifulSoup`][5].

The most interesting part of these script is the modification to `BeautifulSoup`, in order to support variable `tabstop` width in pretty printing. The patch is [here][7]: it basically allows a user to set `tabstop` width as an environmental variable (`$tabstop`) which defaults to "4".

For example:

    % echo '<a><b>text text</b><c>more text</c></a>' | htmlind
    <a>
        <b>
            text text
        </b>
        <c>
            more text
        </c>
    </a>

    % tabstop=1 echo '<a><b>text text</b><c>more text</c></a>' | htmlind
    <a>
     <b>
      text text
     </b>
     <c>
      more text
     </c>
    </a>

   [1]: /blog/tag/useful-scripts/
   [2]: http://acme.cat-v.org/
   [3]: https://github.com/lbolla/cmd/blob/master/htmlind
   [4]: https://github.com/lbolla/cmd/blob/master/xmlind
   [5]: https://github.com/lbolla/cmd/blob/master/pylib/BeautifulSoup.py
   [6]: http://docs.python.org/2/library/xml.dom.minidom.html
   [7]: https://github.com/lbolla/cmd/commit/0079356bab483b5739748e170f4c6bedef0e5b84
