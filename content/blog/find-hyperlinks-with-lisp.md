---
categories:
  - "programming"
date: "2010-10-23"
description: "Script to find hyperlinks in an HTML page"
tags:
  - "lisp"
title: "Find hyperlinks with lisp"
---

Here is a quick-and-dirty script to extract all the unique links from a web
page.

It uses [cl-ppcre][1] to extract the hyperlinks-like strings from a target
string. Tested using [drakma][2] as web client.
    
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
    
There are 139 links on this page...

   [1]: http://weitz.de/cl-ppcre/
   [2]: http://weitz.de/drakma/
