---
categories:
  - "links"
date: "2011-12-17"
description: "YouTube is broken for some links"
tags:
  - "youtube"
title: "500 on YouTube on non-existing videos"
---

Now, [this is embarassing...][1] It looks like requesting a non-existent video on YouTube causes a "500 Internal Server Error"!

![500 on YouTube][2]

For example: 

* Valid url: <http://www.youtube.com/watch?v=b5CeNunbHto>
* Invalid url: <http://www.youtube.com/watch?v=wtf>

Surely, a better response would be something like the one returned when the `videoId` is missing: <http://www.youtube.com/watch?v=>. It seems like [predictions became true][3].

  [1]: http://www.youtube.com/watch?v=wtf
  [2]: /blog/img/capture.jpg (500 on Youtube)
  [3]: http://www.youtube.com/watch?v=OxXc_fXxMoE
