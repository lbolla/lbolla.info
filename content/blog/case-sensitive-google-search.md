# case sensitive Google search

- title: case sensitive Google search
- author: lbolla
- category: programming
- tags: bookmarklet,case,extension,firefox,google,search,sensitive
- summary: 
- post_id: 257
- date: 2011-04-13 17:26:36
- post_date_gmt: 2011-04-13 17:26:36
- comment_status: open
- post_name: case-sensitive-google-search
- status: publish
- post_type: post

----------------

[caption id="attachment_259" align="alignnone" width="300" caption="Case Sensitive Google Search in action"]![Case Sensitive Google Search][1][/caption] Google does not support ["case sensitive" searches][2] (and [here][3] and [here][4]). it does seem to return [slightly different results][5] depending on the case of the search query, but if you are only interested in the exact "case sensitive" matches you're on your own. to solve this problem, I've written a small JS snippet that shades results from Google searches if not exactly matching the case-sensitive search query. you can download it as: 

  * [Case Sensitive Search Firefox Extension][6]: it works with Firefox 3 and 4.
  * [Case Sensitive Search Bookmarklet][7]: just drag-n-drop this link to your list of bookmarks and click it when on a Google search page.
let me know what you think!

   [1]: http://lbolla.info/blog/wp-content/uploads/2011/04/Screen-shot-2011-04-13-at-15.27.29-300x252.png (Case Sensitive Google Search)
   [2]: http://www.google.com/support/websearch/bin/answer.py?hl=en&answer=134479
   [3]: http://www.google.com/support/forum/p/Web+Search/thread?tid=282a99b488daa33f&hl=en
   [4]: http://www.google.com/support/forum/p/Web%20Search/thread?tid=654360f674f696e7&hl=en
   [5]: http://www.labnol.org/internet/search/case-sensitive-google-search/6279/
   [6]: https://github.com/lbolla/junk/raw/master/cssearch/bin/cssearch.xpi
   [7]: javascript:(function(){var s = document.createElement('script'); s.setAttribute('type', 'text/javascript'); s.setAttribute('src', 'http://lbolla.info/cssearch/js'); document.getElementsByTagName('head')[0].appendChild(s);})();