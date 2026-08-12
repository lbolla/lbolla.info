---
title: Useful scripts - htmlind and xmlind
date: 2012-11-23
tags:
- programming
- python
---
This is the forth post of a series describing simple scripts that I wrote to ease my life as a programmer.

In this post I\'ll describe 2 simple scripts to indent nicely `HTML` and `XML` files. I use them primarily with [`acme`](http://acme.cat-v.org/), to pipe selected text and get back nicely formatted output.

Code is available here: [`htmlind`](https://github.com/lbolla/cmd/blob/master/htmlind) and [`xmlind`](https://github.com/lbolla/cmd/blob/master/xmlind). Both programs are written in Python and make use of specialized libraries freely available online. In particular, `xmlind` uses [`xml.dom.minidom`](https://docs.python.org/2/library/xml.dom.minidom.html), included in Python\'s standard library, and `htmlind` uses a modified version of [`BeautifulSoup`](https://github.com/lbolla/cmd/blob/master/pylib/BeautifulSoup.py).

The most interesting part of these script is the modification to `BeautifulSoup`, in order to support variable `tabstop` width in pretty printing. The patch is [here](https://github.com/lbolla/cmd/commit/0079356bab483b5739748e170f4c6bedef0e5b84): it basically allows a user to set `tabstop` width as an environmental variable (`$tabstop`) which defaults to \"4\".

For example:

``` shell
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
```
