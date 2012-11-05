# sleepsort

- author: lbolla
- category: programming
- tags: lisp
- summary: 
- date: 2011-06-17 14:42:37

----------------

To honor [the funniest thread in months][1], here is a lisp implementation of [sleepsort][2]!

    (use-package :sb-thread)
     
    (defun show (item)
      (sleep item)
      (format t "~S~%" item))
     
    (defun sleep-sort (lst)
      (mapcar
        #'(lambda (item) (make-thread #'(lambda () (show item))))
        lst))

   [1]: http://dis.4chan.org/read/prog/1295544154
   [2]: http://en.wikipedia.org/wiki/Sleep_sort
