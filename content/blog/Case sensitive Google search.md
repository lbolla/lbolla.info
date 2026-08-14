---
title: Case sensitive Google search
date: 2011-04-13
---
![Case Sensitive Google Search](Screen-shot-2011-04-13-at-15.27.29-300x252.png)

Google does not support [\"case sensitive\" searches](http://www.google.com/support/websearch/bin/answer.py?hl=en&answer=134479) (and [here](http://www.google.com/support/forum/p/Web+Search/thread?tid=282a99b488daa33f&hl=en) and [here](http://www.google.com/support/forum/p/Web%20Search/thread?tid=654360f674f696e7&hl=en)). It does seem to return [slightly different results](http://www.labnol.org/internet/search/case-sensitive-google-search/6279/) depending on the case of the search query, but if you are only interested in the exact \"case sensitive\" matches you\'re on your own.

To solve this problem, I\'ve written a small Javascript snippet that shades results from Google searches if not exactly matching the case-sensitive search query.

You can download it as:

-   [Case Sensitive Search Firefox Extension](https://github.com/lbolla/junk/raw/master/cssearch/bin/cssearch.xpi): it works with Firefox 3 and 4.
-   Case Sensitive Search Bookmarklet: just create a bookmark using the following code as url and click it when on a Google search page.

```js
javascript:(function(){var s = document.createElement('script'); s.setAttribute('type', 'text/javascript'); s.setAttribute('src', 'https://lbolla.info/cssearch/js'); document.getElementsByTagName('head')[0].appendChild(s);})();
```

A demo is available [here](file:///junk/case_sensitive_search/).

Let me know what you think!
