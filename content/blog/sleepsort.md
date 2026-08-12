---
title: sleepsort
date: 2011-06-17
tags:
- programming
---
To honor [the funniest thread in months](http://dis.4chan.org/read/prog/1295544154), here is a lisp implementation of [sleepsort](http://en.wikipedia.org/wiki/Sleep_sort)!

``` {.commonlisp org-language="lisp"}
(use-package :sb-thread)

(defun show (item)
    (sleep item)
    (format t "~S~%" item))

(defun sleep-sort (lst)
    (mapcar
    #'(lambda (item) (make-thread #'(lambda () (show item))))
    lst))
```
