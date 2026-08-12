---
title: Find hyperlinks with lisp
date: 2010-10-24
tags:
- programming
- lisp
---
Here is a quick-and-dirty script to extract all the unique links from a web page.

It uses [cl-ppcre](http://weitz.de/cl-ppcre/) to extract the hyperlinks-like strings from a target string. Tested using [drakma](http://weitz.de/drakma/) as web client.

```
(asdf:oos 'asdf:load-op :drakma)
(asdf:oos 'asdf:load-op :cl-ppcre)

(defparameter *url-re* "href *= *['"](\S+)['"]")

(defun find-links (str)
  (let ((urls '()))
    (ppcre:do-register-groups
      (u) (*url-re* str nil :start 0 :sharedp t)
      (pushnew u urls :test #'equalp))
  (nreverse urls)))

(print
  (find-links (drakma:http-request "http://lbolla.wordpress.com")))
```

There are 139 links on this page...
