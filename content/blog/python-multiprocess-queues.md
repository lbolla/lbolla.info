---
categories:
  - "programming"
date: "2016-04-25"
description: "Surprising behaviour when using Queues in a blocking or non-blockingi way."
tags:
  - "python"
title: "Comparison of blocking and non-blocking Python's multiprocessing Queue"
---

Python's [multiprocessing][1] module offers a `Queue` implementation.
Surprisingly enough (for me at least), its performance varies greatly if used in a blocking or non-blocking fashion. In particular, the non-blocking way is about *ten times slower* than the blocking one!

Consider this code, which feeds a Queue and then drains it in a blocking and non-blocking way:

<script src="https://gist.github.com/lbolla/92bad9f4320940ac2f762424ac840a12.js"></script>

Running it on my machine, with Python 2.7, gives me these results (Python 3.4 results are similar, but less dramatic):

    feed=0.599231004715 drain=0.964730024338 drain_nowait=8.39909696579

As you can see, `drain_nowait` is about 10x slower than `drain`. I suspect there is some serious lock-contention going on, but I have not yet pinpointed where, exactly! In the meantime, I think I'll stick with the blocking code...

  [1]: https://docs.python.org/2/library/multiprocessing.html#multiprocessing.Queue
