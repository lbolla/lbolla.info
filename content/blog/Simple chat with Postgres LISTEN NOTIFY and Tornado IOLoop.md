---
title: Simple chat with Postgres LISTEN NOTIFY and Tornado IOLoop
date: 2013-03-21
tags:
- programming
- tornado
---
Postgres supports from version 8.4 a very interesting functionality: [LISTEN](http://www.postgresql.org/docs/9.2/static/sql-listen.html)/[NOTIFY](http://www.postgresql.org/docs/9.2/static/sql-notify.html) allows sending asynchronous messages to clients connected to the database.

As in a normal \"chat\", a client \"subscribed\" (`LISTEN`) to a channel receives all the messages that other clients \"sent\" (`NOTIFY`) on that channel.

Since version 9.0, a notification message can have a payload string as long as 8000 bytes.

In order to experiment with this feature, I\'ve implemented a simple chat based on Tornado\'s [IOLoop](http://www.tornadoweb.org/en/stable/ioloop.html). Each client subscribes to a channel (or \"room\" in chat jargon) and listens to it [adding a callback](http://www.tornadoweb.org/en/stable/ioloop.html#tornado.ioloop.IOLoop.add_handler) to react to a new notification. In the meantime, in another thread, the client is free to write and submit messages to the \"room\". Here is a screenshot of the chat in action:

![Chatting at London Chess Candidates 2013](/img/chat.png

This is the code, available also on [gist](https://gist.github.com/lbolla/5213919):

<script src="https://gist.github.com/lbolla/5213919.js"></script>
