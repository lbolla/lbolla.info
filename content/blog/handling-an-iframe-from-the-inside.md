# handling an iframe from the inside

- title: handling an iframe from the inside
- author: lbolla
- category: programming
- tags: iframe,javascript,move,postMessage,resize,same origin policy
- summary: 
- post_id: 241
- date: 2011-03-30 19:19:30
- post_date_gmt: 2011-03-30 17:19:30
- comment_status: open
- post_name: handling-an-iframe-from-the-inside
- status: publish
- post_type: post

----------------

if you've ever worked with iframes you've certainly run into the [same origin policy][1].

from [here][2]:

> The same origin policy basically limits how scripts and frames on different domains can talk to each other. 

this is particularly bad if you want to resize an iframe to accomodate its content, as this is not doable with simple CSS (to the best of my knowledge!). it can be done using `[window.postMessage`][3], though.

[see a demo here][4].

basically, the content of the iframe fires `postMessage`s to its parent window and the window itself, i.e. the iframe container, handles them. cool...

   [1]: http://en.wikipedia.org/wiki/Same_origin_policy
   [2]: http://www.onlineaspect.com/2010/01/15/backwards-compatible-postmessage/
   [3]: https://developer.mozilla.org/en/DOM/window.postMessage
   [4]: http://lbolla.info/junk/iframe/