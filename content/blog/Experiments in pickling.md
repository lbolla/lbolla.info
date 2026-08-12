---
title: Experiments in pickling
date: 2014-05-14
tags:
- programming
- python
---
[`pickle`](https://docs.python.org/2/library/pickle.html) is a standard library module to serialize and deserialize Python objects. Being written in pure Python, it\'s fairly slow, so the standard library provides a pure-C implementation, called [`cPickle`](https://docs.python.org/2/library/pickle.html#module-cPickle), with the limitation that it cannot be [subclassed](http://doughellmann.com/2007/06/24/pymotw-pickle-and-cpickle.html).

What\'s interesting about `cPickle` are two little known settings that can speed up serialization quite substantially.

1.  [`cPickle.HIGHEST_PROTOCOL`](https://docs.python.org/2/library/pickle.html#pickle.HIGHEST_PROTOCOL) basically dumps a Python object using a binary protocol, rather than the default ASCII-based, more portable, protocol 0. If portability or backward compatibility are not an issue for you, you should use it: it\'s documented and probably here to stay.

2.  [`Pickler`](https://docs.python.org/2/library/pickle.html#pickle.Pickler)\'s undocumented `fast` flag. It turns out that `cPickle` implementation has a \"fast mode\" that is enabled by setting this `fast` flag to `True`. It\'s undocumented so probably subject to change, but it makes dumping objects way faster.

Looking at the [implementation](http://hg.python.org/cpython/file/c5464268aead/Modules/_pickle.c#l548) of `cPickle`, the comments in the code have something to say about \"fast mode\":

> The fast mode disable the usage of memo, therefore speeding the pickling process by not generating superfluous PUT opcodes. It should not be used if with self-referential objects.

[memo](https://docs.python.org/2/library/pickle.html#pickle.Pickler.clear_memo) is basically a cache, within the pickler, that remembers what objects have already been processed, used mainly to avoid infinite loops when dumping self-referential data structures. But if you are dumping data structures that do not reference themselves, you can spare some time disabling this caching.

To test these settings, I compared \"vanilla\" `cPickle.dumps`, with \"highest\\~protocol~\" and \"fast mode\", for 3 different objects: a small, a medium and a large list of dictionaries. The code is available in [`gist`](https://gist.github.com/lbolla/1bec1b70ef9c8e254b57):

<script src="https://gist.github.com/lbolla/1bec1b70ef9c8e254b57.js"></script>

Clone it and run it:

```shell
$> git clone https://gist.github.com/1bec1b70ef9c8e254b57.git pickle_experiments
$> cd pickle_experiments
$> sh run.sh
```

On my machine, I get these results:

```
SMALL
dumps
10 loops, best of 3: 7.39 usec per loop
highp
10 loops, best of 3: 2.5 usec per loop
pickl
10 loops, best of 3: 4.1 usec per loop

MEDIUM
dumps
10 loops, best of 3: 705 usec per loop
highp
10 loops, best of 3: 206 usec per loop
pickl
10 loops, best of 3: 111 usec per loop

LARGE
dumps
3 loops, best of 3: 1.34 sec per loop
highp
10 loops, best of 3: 823 msec per loop
pickl
10 loops, best of 3: 135 msec per loop
```

*Note: I\'ve reduced the number of iterations to 3 for \"vanilla LARGE\" because it was taking too long...*

\"high\\~protocol~\" is between 2 and 3 times faster than \"vanilla\" for all objects, and **\"fast mode\" is 6 times faster than \"high\\~protocol~\" and 10 times faster than \"vanilla\" for large objects**!
