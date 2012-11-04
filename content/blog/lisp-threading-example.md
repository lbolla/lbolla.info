# lisp threading example

- author: lbolla
- category: programming
- tags: lisp
- summary: Example of threading programming in Lisp
- date: 2010-10-23 15:31:34

----------------

Today I wanted to experiment with threads in lisp ([sbcl][1], in particular).

Here is a trivial example of how to access a shared resource (a closure,
keeping a list of integers), from a set of `*nt*` threads.
    
    (use-package :sb-thread)
    
    ;; number of threads
    (defparameter *nt* 10)
    
    ;; threads
    (defvar *threads* '())
    
    ;; mutex to use with shared resource accessed by the threads
    (defvar *a-mutex* (make-mutex :name "acc-lock"))
    
    ;; shared closure accessed by the threads
    (let ((x '()))
      (defun acc (v)
        (with-mutex (*a-mutex*)
                    (push v x)))
      (defun get-acc ()
        x))
    
    ;; print the shared resource
    (print (get-acc))
    
    ;; wait for all the threads to return
    (mapcar #'join-thread
            ;; run the threads
            (loop :for i :below *nt*   
                  ;; bind i to x so it is local to the thread
                  :collect (let ((x i))
                            (make-thread #'(lambda ()
                                             ;; body of the thread
                                             (sleep (random 2))
                                             (acc x))
                                         :name x))))
    
    ;; print the shared resource
    (print (get-acc))
    

It can't get much simpler than that...

   [1]: http://www.sbcl.org/
