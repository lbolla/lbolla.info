---
categories:
  - "programming"
date: "2012-09-02"
description: "None"
tags:
  - "benchmark"
  - "haskell"
  - "python"
  - "tornado"
  - "warp"
  - "yesod"
title: "Tornado vs. Warp vs. Yesod"
aliases:
  - /blog/2012/09/02/tornado-vs.-warp-vs.-yesod
---

Today I tried to benchmark 3 web servers that I've used recently: 

  1. [Tornado][1]
  2. [Warp][2]
  3. [Yesod][3]

In fact, these are only **2** web servers, because `Yesod` runs on top of Warp
and it's a fully fledged web framework, rather than a web server: but this was
also the intent of the benchmark, i.e. to measure how slower all its goodies
made Yesod with respect to Warp.

Tornado and Warp are obviously very different
web servers (async vs. threaded, interpreted vs. compiled, etc.) but, [who
cares][4]?

The benchmark is very simple: a single handler returning "Hello
World", very original. Obviously, this is hardly a real world example, but it
can give indications even if only with "orders of magnitude" of approximation.

Nonetheless, the results were very interesting. First of all, here is the code.

### Tornado

<script src="https://gist.github.com/3567006.js?file=tornadoweb.py"></script>

### Warp

<script src="https://gist.github.com/3567006.js?file=warp.hs"></script>

### Yesod

<script src="https://gist.github.com/3567006.js?file=yesod"></script>

And the results, obtained using httperf:

    $> httperf --hog --client=0/1 --server=localhost --port=8080 --uri=/ --rate=1000 --send-buffer=4096 --recv-buffer=16384 --num-conns=100 --num-calls=100 --burst-length=20

<table>
<tr>
<th>Tornado</th>
<td>518 req/s</td>
</tr>
<tr>
<th>Warp</th>
<td>10079 req/s</td>
</tr>
<tr>
<th>Yesod</th>
<td>929 req/s</td>
</tr>
<tr>
<th>Yesod w/o session management</th>
<td>7924 req/s</td>
</tr>
</table>

Wait! _What?!_ Yesod is 10 times slower than Warp!?

I asked an explanation to the Yesod developers and [they tracked down the
issue][5]: the work of these guys is an example worth studying of how to
benchmark and debug code! Anyway, it looks like the issue is that serializing
timestamps is incredibly inefficient: I hope a patch will be ready soon! In the
meantime, I strongly suggest you to disable session management from Yesod if
you want high performance. _(In the code shown, I've also disabled Hamlet,
Yesod's templating system, but it turned out that it didn't make much
difference: [code using Hamlet is in gist][6].)_

Overall, though, even on my crappy single-core old laptop, the result is
amazing: Warp/Yesod is ~20 times faster than one of the fastest Python web
servers.

   [1]: http://www.tornadoweb.org/ (Tornado)
   [2]: http://hackage.haskell.org/package/warp/ (Warp)
   [3]: http://www.yesodweb.com/ (Yesod)
   [4]: http://ziutek.github.com/web_bench/
   [5]: https://github.com/yesodweb/yesod/issues/415
   [6]: https://gist.github.com/3567006/76f6245c21adc5576f201bcf83437269e8f56d93
