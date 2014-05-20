---
categories:
  - "programming"
date: "2010-08-04"
description: "A simple lisp client to talk to Wordpress"
tags:
  - "lisp"
  - "wordpress"
title: "Simple Wordpress API lisp client"
---

I like old things, therefore I started to learn Lisp.

There isn't a better way to learn than by doing, so I tried to implement a
client for the [wordpress api][1]. the result, even if not complete yet, it's
so elegant that I'd like to [share it][2].
    
    (require 's-xml-rpc)
    
    (defpackage :wp 
      (:use :cl :cl-user :s-xml-rpc))
    
    (in-package :wp)
    
    (defparameter +interfaces+ 
      '((get-blogs "wp.getUsersBlogs" username password)
        (get-tags "wp.getTags" blog-id username password)
        (get-comment-count "wp.getCommentCount" blog-id username password post-id)
        (get-post-status-list "wp.getPostStatusList" blog-id username password)
        (get-page-status-list "wp.getPageStatusList" blog-id username password)
        (get-page-templates "wp.getPageTemplates" blog-id username password)
        (get-options "wp.getOptions" blog-id username password)
        (delete-comment "wp.deleteComment" blog-id username password comment-id)
        (get-comment-status-list "wp.getCommentStatusList" blog-id username password)
        (get-page "wp.getPage" blog-id page-id username password)
        (get-pages "wp.getPages" blog-id username password)
        (get-page-list "wp.getPageList" blog-id username password)
        (delete-page "wp.deletePage" blog-id username password page-id)
        (get-authors "wp.getAuthors" blog-id username password)
        (get-categories "wp.getCategories" blog-id username password)
        (delete-category "wp.deleteCategory" blog-id username password category-id)
        (suggest-categories "wp.suggestCategories" blog-id username password category max-results)
        (get-comment "wp.getComment" blog-id username password comment-id))
      "Interface definition to WP services")
    
    (defun defunwp (params) 
      (destructuring-bind (name service &rest rest) params
        (setf (fdefinition name) (compile nil `(lambda (host ,@rest &optional (url "/xmlrpc.php")) 
                                                 (block ,name 
                                                        (xml-rpc-call 
                                                          (encode-xml-rpc-call ,service ,@rest)
                                                          :host host
                                                          :url url)))))
        name))
    
    (mapcar #'(lambda (interface) (export (defunwp interface))) +interfaces+)
    
    

It uses the [s-xml-rpc][3] package and I've tested it with [SBCL][4].

Example usage is as follows:
    
    (wp:get-blogs "username.wordpress.com" "your-username" "your-password") ; returns the list of blogs for the user
    (wp:get-pages "username.wordpress.com" your-blog-id "your-username" "your-password") ; returns the list of pages

And so on (see `wp::+interfaces+` for function names and required params).

Enjoy!

   [1]: http://codex.wordpress.org/XML-RPC_Support
   [2]: http://github.com/lbolla/junk/blob/master/lisp/wordpress.lisp
   [3]: http://common-lisp.net/project/s-xml-rpc/
   [4]: http://www.sbcl.org/
