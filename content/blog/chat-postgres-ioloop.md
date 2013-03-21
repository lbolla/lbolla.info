# Simple chat with Postgres LISTEN/NOTIFY and Tornado's IOLoop

- author: lbolla
- category: programming
- tags: tornado,postgres,python
- summary: Simple chat implemented with Tornado's IOLoop and Postgres LISTEN/NOTIFY
- date: 2013-03-21 16:00:00

----------------

Postgres supports from version 8.4 a very interesting functionality:
[LISTEN][1]/[NOTIFY][2] allows sending asynchronous messages to clients
connected to the database.

As in a normal "chat", a client "subscribed" (`LISTEN`) to a channel receives
all the messages that other clients "sent" (`NOTIFY`) on that channel.

Since version 9.0, a notification message can have a payload string as long as
8000 bytes.

In order to experiment with this feature, I've implemented a simple chat based
on Tornado's [IOLoop][3]. Each client subscribes to a channel (or "room" in
chat jargon) and listens to it [adding a callback][5] to react to a new
notification. In the meantime, in another thread, the client is free to write
and submit messages to the "room". Here is a screenshot of the chat in action:

![Chatting at London Chess Candidates 2013][6]

This is the code, available also on [gist][4]:

<script src="https://gist.github.com/lbolla/5213919.js"></script>


   [1]: http://www.postgresql.org/docs/9.2/static/sql-listen.html
   [2]: http://www.postgresql.org/docs/9.2/static/sql-notify.html
   [3]: http://www.tornadoweb.org/en/stable/ioloop.html
   [4]: https://gist.github.com/lbolla/5213919
   [5]: http://www.tornadoweb.org/en/stable/ioloop.html#tornado.ioloop.IOLoop.add_handler
   [6]: /blog/img/chat.png (Chatting example)
