---
title: Javascript templating benchmark
date: 2011-05-23
tags:
- programming
- javascript
---
There are many popular libraries to do templating in Javascript.

The most popular are:

-   [JQuery Template](http://api.jquery.com/jQuery.template/)
-   [Pure Template](http://www.javascriptr.com/2008/06/05/purejstemplate-a-pure-javascript-templating-engine-for-jquery/)
-   [Resig Template](http://ejohn.org/blog/javascript-micro-templating/)
-   [Trimpath Template](http://code.google.com/p/trimpath/wiki/JavaScriptTemplates)
-   [JQote2 Template](http://aefxx.com/jquery-plugins/jqote2/)

I decided to benchmark them, so I created a simple \"hello world\" test.

As usual, the results are interesting. Here are, on my box:

|                 | Firefox 3.6 | Chrome 11.0 | Safari 5.0 |
| --------------- | ----------- | ----------- | ---------- |
| jQuery Template | 297ms       | 138ms       | 113ms      |
| Pure            | 309ms       | 43ms        | 36ms       |
| Resig           | 309ms       | 41ms        | 41ms       |
| Trimpath        | 15ms        | 5ms         | 6ms        |
| JQote2          | 7ms         | 1ms         | 6ms        |

A part from the obvious result that Firefox is the slowest browser of all, I\'m astonished by the excellent performance of JQote2!
