# get registered domain in Python and Javascript

- title: get registered domain in Python and Javascript
- author: lbolla
- category: programming
- tags: domain,javascript,python,registered
- summary: 
- post_id: 243
- date: 2011-04-05 15:08:14
- post_date_gmt: 2011-04-05 13:08:14
- comment_status: open
- post_name: get-registered-domain-in-python-and-javascript
- status: publish
- post_type: post

----------------

[reg-dom-libs][1] are a set of libraries for `C`, `PHP` and `Perl` to convert an arbitrary domain name to the registered domain name. 

  * for simple domains, like `www.amazon.com` or `news.ycombinator.com`, the task is trivial.
  * for more complicated ones, like `www.ebay.co.uk` or `www.japantimes.co.jp`, handling the second level subdomain is a little painful.
  * for exoteric ones, like `nic.com.ai` or `www.nic.net.ge` or `公司.cn`, the problem becomes virtually impossible.
  * after seeing stupid ones, like `www.comune.caserta.it` (believe it or not, the registered domain is `comune.caserta.it`!), I gave up finding an elegant algorithm for the problem.
  * a full list of valid registered domain is necessary. luckily, it is available (and nightly updated) [here][2].
inspired by [reg-dom-libs][1], I've ported the algorithm to [Python][3] and [Javascript][4]. see the tests at the end of each file for an example of the usage. a demo is availble [here][5].

   [1]: http://www.dkim-reputation.org/regdom-libs/
   [2]: http://mxr.mozilla.org/mozilla-central/source/netwerk/dns/effective_tld_names.dat?raw=1
   [3]: https://github.com/lbolla/junk/blob/master/utils/regdomain.py
   [4]: https://github.com/lbolla/junk/blob/master/utils/regdomain.js
   [5]: http://lbolla.info/junk/regdomain/