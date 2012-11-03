# 500 on YouTube on non-existing videos

- author: lbolla
- category: links
- date: 2011-12-17 15:27:01
- summary: YouTube is broken for some links
- tags: youtube

----------------

Now, [this is embarassing...][1] It looks like requesting a non-existent video on YouTube causes a "500 Internal Server Error"!

![500 on YouTube][2]

For example: 

* Valid url: <http://www.youtube.com/watch?v=b5CeNunbHto>
* Invalid url: <http://www.youtube.com/watch?v=wtf>

Surely, a better response would be something like the one returned when the `videoId` is missing: <http://www.youtube.com/watch?v=>. It seems like [predictions became true][3].

  [1]: http://www.youtube.com/watch?v=wtf
  [2]: http://lbolla.info/blog/wp-content/uploads/2011/12/capture.jpg (500 on Youtube)
  [3]: http://www.youtube.com/watch?v=OxXc_fXxMoE
