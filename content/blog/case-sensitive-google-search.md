---
categories:
  - "programming"
date: "2011-04-13"
description: "Hack to simplify case sensitive searches on Google"
tags:
  - "bookmarklet"
  - "extension"
  - "firefox"
  - "google"
  - "javascript"
title: "Case sensitive Google search"
---

![Case Sensitive Google Search][1]

Google does not support ["case sensitive" searches][2] (and [here][3] and
[here][4]). It does seem to return [slightly different results][5] depending on
the case of the search query, but if you are only interested in the exact "case
sensitive" matches you're on your own.

To solve this problem, I've written a small Javascript snippet that shades
results from Google searches if not exactly matching the case-sensitive search
query.

You can download it as: 

  * [Case Sensitive Search Firefox Extension][6]: it works with Firefox 3 and 4.
  * Case Sensitive Search Bookmarklet: just create a bookmark using the
    following code as url and click it when on a Google search page.

        javascript:(function(){var s = document.createElement('script'); s.setAttribute('type', 'text/javascript'); s.setAttribute('src', 'https://lbolla.info/cssearch/js'); document.getElementsByTagName('head')[0].appendChild(s);})();

A demo is available [here][7].

Let me know what you think!

   [1]: /blog/img/Screen-shot-2011-04-13-at-15.27.29-300x252.png (Case Sensitive Google Search)
   [2]: http://www.google.com/support/websearch/bin/answer.py?hl=en&answer=134479
   [3]: http://www.google.com/support/forum/p/Web+Search/thread?tid=282a99b488daa33f&hl=en
   [4]: http://www.google.com/support/forum/p/Web%20Search/thread?tid=654360f674f696e7&hl=en
   [5]: http://www.labnol.org/internet/search/case-sensitive-google-search/6279/
   [6]: https://github.com/lbolla/junk/raw/master/cssearch/bin/cssearch.xpi
   [7]: /junk/case_sensitive_search/
