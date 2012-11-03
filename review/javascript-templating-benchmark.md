# javascript templating benchmark

- title: javascript templating benchmark
- author: lbolla
- category: programming
- tags: 
- summary: 
- post_id: 271
- date: 2011-05-23 09:47:46
- post_date_gmt: 2011-05-23 09:47:46
- comment_status: open
- post_name: javascript-templating-benchmark
- status: publish
- post_type: post

----------------

there are many popular libraries to do templating in javascript.

the most popular are:

  * [JQuery Template][1]
  * [Pure Template][2]
  * [Resig Template][3]
  * [Trimpath Template][4]
  * [JQote2 Template][5]

I decided to benchmark them, so I created a simple "hello world" test. you can find it [here][6].

as usual, the results are interesting. here are, on my box:

Firefox 3.6Chrome 11.0Safari 5.0

JQuery Template
297ms
138ms
113ms

Pure
309ms
43ms
36ms

Resig
309ms
41ms
41ms

Trimpath
15ms
5ms
6ms

JQote2
_7ms_
_1ms_
6ms

a part from the obvious result that Firefox is the slowest browser of all, I'm astonished by the excellent performance of JQote2!

   [1]: http://api.jquery.com/jQuery.template/
   [2]: http://www.javascriptr.com/2008/06/05/purejstemplate-a-pure-javascript-templating-engine-for-jquery/
   [3]: http://ejohn.org/blog/javascript-micro-templating/
   [4]: http://code.google.com/p/trimpath/wiki/JavaScriptTemplates
   [5]: http://aefxx.com/jquery-plugins/jqote2/
   [6]: /junk/js/tmpl.html