# HSGrep: Sorted Grep in Haskell

- title: HSGrep: Sorted Grep in Haskell
- author: lbolla
- category: programming
- tags: grep,haskell,sorted
- summary: 
- post_id: 363
- date: 2011-11-27 16:30:40
- post_date_gmt: 2011-11-27 16:30:40
- comment_status: open
- post_name: hsgrep-sorted-grep-in-haskell
- status: publish
- post_type: post

----------------

As an exercise to learn [Haskell][1], I wrote a specialized grep to work on sorted files. It uses [binary search][2] to scan a text file and print all the (consecutive) lines that start with a user defined string. My program is a rewrite of [sgrep][3] in [Haskell][1]: I called it [HSGrep][4]. Code is available on [github][5]. Thanks a lot for [all your useful suggestions][6]! As soon as possible, I'll post some benchmarking [here][7]. (EDIT: [benchmarks now available!][7]) After downloading the [source code][4], build install and run it with: [shell] $> cabal build $> cabal install $> hslint <string> <filename> [/shell]

   [1]: http://haskell.org/haskellwiki/Haskell (Haskell)
   [2]: http://en.wikipedia.org/wiki/Binary_search_algorithm
   [3]: http://sourceforge.net/projects/sgrep/ (sgrep)
   [4]: https://github.com/lbolla/HSGrep
   [5]: https://github.com/lbolla/HSGrep (HSGrep)
   [6]: http://codereview.stackexchange.com/q/6318/8638
   [7]: http://lbolla.info/blog/2011/11/30/hsgrep-benchmarking/