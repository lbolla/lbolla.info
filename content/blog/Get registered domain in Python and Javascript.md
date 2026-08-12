---
title: Get registered domain in Python and Javascript
date: 2011-04-05
tags:
- programming
- python
- javascript
---
[reg-dom-libs](http://www.dkim-reputation.org/regdom-libs/) are a set of libraries for `C`, `PHP` and `Perl` to convert an arbitrary domain name to the registered domain name.

-   For simple domains, like `www.amazon.com` or `news.ycombinator.com`, the task is trivial.
-   For more complicated ones, like `www.ebay.co.uk` or `www.japantimes.co.jp`, handling the second level subdomain is a little painful.
-   For exoteric ones, like `nic.com.ai` or `www.nic.net.ge` or `公司.cn`, the problem becomes virtually impossible.
-   After seeing stupid ones, like `www.comune.caserta.it` (believe it or not, the registered domain is `comune.caserta.it`!), I gave up finding an elegant algorithm for the problem.
-   A full list of valid registered domain is necessary. Luckily, it is available (and nightly updated) [here](http://mxr.mozilla.org/mozilla-central/source/netwerk/dns/effective_tld_names.dat?raw=1).

Inspired by [reg-dom-libs](http://www.dkim-reputation.org/regdom-libs/), I\'ve ported the algorithm to [Python](https://github.com/lbolla/junk/blob/master/utils/regdomain.py) and [Javascript](https://github.com/lbolla/junk/blob/master/utils/regdomain.js). See the tests at the end of each file for an example of the usage. A demo is available [here](file:///junk/regdomain/).
