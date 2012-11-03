# find hyperlinks with lisp

- title: find hyperlinks with lisp
- author: lbolla
- category: programming
- tags: cl-ppcre,drakma,links,lisp,urls
- summary: 
- post_id: 226
- date: 2010-10-23 15:55:30
- post_date_gmt: 2010-10-23 13:55:30
- comment_status: open
- post_name: find-hyperlinks-with-lisp
- status: publish
- post_type: post

----------------

here is a quick-and-dirty script to extract all the unique links from a web page.

it uses [cl-ppcre][1] to extract the hyperlinks-like strings from a target string. tested using [drakma][2] as web client.
    
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
    

there are 139 links on this page...

   [1]: http://weitz.de/cl-ppcre/
   [2]: http://weitz.de/drakma/