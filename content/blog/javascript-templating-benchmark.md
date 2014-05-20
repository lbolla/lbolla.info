---
categories:
  - "programming"
date: "2011-05-23"
description: "None"
tags:
  - "javascript"
  - "benchmark"
title: "Javascript templating benchmark"
---

There are many popular libraries to do templating in Javascript.

The most popular are:

  * [JQuery Template][1]
  * [Pure Template][2]
  * [Resig Template][3]
  * [Trimpath Template][4]
  * [JQote2 Template][5]

I decided to benchmark them, so I created a simple "hello world" test. You can
find it [here][6].

As usual, the results are interesting. Here are, on my box:

<table>
<tr>
<th></th>
<th>Firefox 3.6</th>
<th>Chrome 11.0</th>
<th>Safari 5.0</th>
</tr>
<tr>
<td>JQuery Template</td>
<td>297ms</td>
<td>138ms</td>
<td>113ms</td>
</tr>
<tr>
<td>Pure</td>
<td>309ms</td>
<td>43ms</td>
<td>36ms</td>
</tr>
<tr>
<td>Resig</td>
<td>309ms</td>
<td>41ms</td>
<td>41ms</td>
</tr>
<tr>
<td>Trimpath</td>
<td>15ms</td>
<td>5ms</td>
<td>6ms</td>
</tr>
<tr>
<td>JQote2</td>
<td>7ms</td>
<td>1ms</td>
<td>6ms</td>
</tr>
</table>

A part from the obvious result that Firefox is the slowest browser of all, I'm
astonished by the excellent performance of JQote2!

   [1]: http://api.jquery.com/jQuery.template/
   [2]: http://www.javascriptr.com/2008/06/05/purejstemplate-a-pure-javascript-templating-engine-for-jquery/
   [3]: http://ejohn.org/blog/javascript-micro-templating/
   [4]: http://code.google.com/p/trimpath/wiki/JavaScriptTemplates
   [5]: http://aefxx.com/jquery-plugins/jqote2/
   [6]: /junk/js/tmpl.html
