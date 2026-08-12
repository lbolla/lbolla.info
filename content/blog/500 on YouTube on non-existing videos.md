---
title: 500 on YouTube on non-existing videos
date: 2011-12-17
---
Now, [this is embarassing...](http://www.youtube.com/watch?v=wtf) It looks like requesting a non-existent video on YouTube causes a \"500 Internal Server Error\"!

![500 on YouTube](capture.jpg)

For example:

-   Valid url: <http://www.youtube.com/watch?v=b5CeNunbHto>
-   Invalid url: <http://www.youtube.com/watch?v=wtf>

Surely, a better response would be something like the one returned when the `videoId` is missing: <http://www.youtube.com/watch?v=>. It seems like [predictions became true](http://www.youtube.com/watch?v=OxXc_fXxMoE).
