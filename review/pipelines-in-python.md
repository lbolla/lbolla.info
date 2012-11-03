# Pipelines in Python

- title: Pipelines in Python
- author: lbolla
- category: programming
- tags: coroutine,generator,pipeline,python
- summary: 
- post_id: 411
- date: 2012-04-20 14:07:10
- post_date_gmt: 2012-04-20 13:07:10
- comment_status: open
- post_name: pipelines-in-python
- status: publish
- post_type: post

----------------

Generators ([PEP 255 "Simple Generators"][1]) and Coroutines ([PEP 342 "Coroutines via Enhanced Generators"][2]) are the cleanest way I've come across so far to implement the concept of a "pipeline" in Python. 

## First approximation

A pipeline is made of: 

  * a _Producer_, that generates data;
  * many _Stage_s, that receive data from the previous stage and send it to the next;
  * a _Consumer_, that receives data from the last stage.
The producer is a coroutine that only _send_s data, generated internally from some initial state. _Stage_s are coroutines that both receive and send messages. The _consumer_ only receives data. Chaining is done in function _pipeline_: each argument but the last is instantiated with an instance of the next stage. The full pipeline is _started_ by issuing a _next_ (or _send(None)_) to the _Producer_. In the following example, a stream of integers is produced and pushed down the pipeline: each stage adds 1 and finally the result is printed in the consumer. [gist id=2428213 file=pipeline_1.py] 

## Wrapping it up

A pattern emerges, so we'd better wrap it up in a class. Moreover, let's split the "architecture" of the pipeline from the behavior of each stage. [gist id=2428213 file=pipeline_3.py] 

## More useful example

As a more interesting application, here is how to use a pipeline to implement a simple crawler, to download links from <http://news.ycombinator.com/> and find all the posts where the word "Python" is mentioned. [gist id=2428213 file=pipeline_4.py] 

## Cleaning things up

Things are still far from clean and bulletproof. One step in the right direction is to follow the suggestions found in [David Beazley's presentation on coroutines][3]. [gist id=2428213 file=pipeline_5.py] The previous examples is by no means "production ready", but maybe someone will find some good idea to apply to real world problems.

   [1]: http://www.python.org/dev/peps/pep-0255/
   [2]: http://www.python.org/dev/peps/pep-0342/
   [3]: http://www.dabeaz.com/Fcoroutines/Coroutines.pdf