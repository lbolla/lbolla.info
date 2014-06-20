---
categories:
  - "programming"
date: "2013-12-02"
description: "Simple chat server implemented with Tornado, Redis and websockets"
tags:
  - "tornado"
  - "redis"
  - "websocket"
title: "Tornado Redis chat"
---

[redis][3] is often described as an "in-memory persistent key-value store", but
[it's much more than that][5]. One of its nicest features is its support for
the [`Publish/Subscribe messaging paradigm`][6], which makes it easy to
implement, for example, a chat server.

In order to learn how to use it, I decided to implement a chat server using
Redis and Tornado. This is a classical exercise, and [others][2] have done the
same: but their solution has some pitfalls that I tried to fix.

The code is forked from [pelletier][2]'s, with some improvements:

* Support for the latest Python Redis's client [redis-py][4] version 2.6.9
* Thread-safety: using the only method in Tornado's IOLoop that is
  [thread-safe][7]
* Tested with Python 3.3

This is the code, available also on [gist][1]:

<script src="https://gist.github.com/lbolla/4754600.js"></script>


   [1]: https://gist.github.com/lbolla/4754600
   [2]: https://gist.github.com/pelletier/532067
   [3]: http://redis.io/
   [4]: http://redis-py.readthedocs.org/en/latest/
   [5]: http://openmymind.net/2012/1/23/The-Little-Redis-Book/
   [6]: http://redis.io/topics/pubsub
   [7]: http://www.tornadoweb.org/documentation/ioloop.html?highlight=add_callback#tornado.ioloop.IOLoop.add_callback
