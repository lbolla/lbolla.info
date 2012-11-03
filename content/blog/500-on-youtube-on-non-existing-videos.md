# 500 on Youtube on non-existing videos

- title: 500 on Youtube on non-existing videos
- author: lbolla
- category: links
- tags: 
- summary: 
- post_id: 377
- date: 2011-12-17 15:27:01
- post_date_gmt: 2011-12-17 15:27:01
- comment_status: open
- post_name: 500-on-youtube-on-non-existing-videos
- status: publish
- post_type: post

----------------

Now, [this is embarassing...][1] It looks like requesting a non-existent video on Youtube causes a "500 Internal Server Error"! 

[caption id="attachment_381" align="aligncenter" width="613" caption="Requesting a non-existing video on Youtube returns 500!"]![500][2][/caption] 

For example: 

  * Valid url: <http://www.youtube.com/watch?v=b5CeNunbHto>
  * Invalid url: <http://www.youtube.com/watch?v=wtf>
Surely, a better response would be something like the one returned when  the videoId is misisng: <http://www.youtube.com/watch?v=> Seems like [predictions became true][3].

   [1]: http://www.youtube.com/watch?v=wtf
   [2]: http://lbolla.info/blog/wp-content/uploads/2011/12/capture.jpg (500 on Youtube)
   [3]: http://www.youtube.com/watch?v=OxXc_fXxMoE