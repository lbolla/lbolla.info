# sleepsort

- title: sleepsort
- author: lbolla
- category: programming
- tags: lisp,sleepsort
- summary: 
- post_id: 279
- date: 2011-06-17 14:42:37
- post_date_gmt: 2011-06-17 14:42:37
- comment_status: open
- post_name: sleepsort
- status: publish
- post_type: post

----------------

to honor [the funniest thread in months][1], here is a lisp implementation of [sleepsort][2]! [clojure] (use-package :sb-thread) (defun show (item) (sleep item) (format t "~S~%" item)) (defun sleep-sort (lst) (mapcar #'(lambda (item) (make-thread #'(lambda () (show item)))) lst)) [/clojure]

   [1]: http://dis.4chan.org/read/prog/1295544154
   [2]: http://en.wikipedia.org/wiki/Sleep_sort