# HSGrep benchmarking

- title: HSGrep benchmarking
- author: lbolla
- category: programming
- tags: benchmark,grep,haskell
- summary: 
- post_id: 369
- date: 2011-11-30 23:38:02
- post_date_gmt: 2011-11-30 23:38:02
- comment_status: open
- post_name: hsgrep-benchmarking
- status: publish
- post_type: post

----------------

Few days ago, [I rewrote sgrep in Haskell][1]. I was curious to know how it compares to [grep][2] in term of execution speed. In particular, I was interested to verify that hsgrep scales as O(log n), instead of O(n), with n being the size of the file analyzed. First of all, in order to have similar performance to grep, I had to convert my original program to use [Haskell's bytestrings][3]. [You can find the code here][4]. Testing files are generated with [this script][5]. Here are the results obtained. grep is still faster for smallish files (I haven't spent too much time tweaking hsgrep), but hsgrep scales much better and it wins for files larger than few megabytes! ![][6]

   [1]: http://lbolla.info/blog/2011/11/27/hsgrep-sorted-grep-in-haskell/
   [2]: http://en.wikipedia.org/wiki/Grep
   [3]: http://hackage.haskell.org/packages/archive/bytestring/latest/doc/html/Data-ByteString.html
   [4]: https://github.com/lbolla/HSGrep/tree/bytestring
   [5]: https://github.com/lbolla/HSGrep/blob/bytestring/data/gendata.hs
   [6]: http://lbolla.info/blog/wp-content/uploads/2011/11/bench1.png (HSGrep benchmark)