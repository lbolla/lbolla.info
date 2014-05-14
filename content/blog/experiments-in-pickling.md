# Experiments in pickling

- author: lbolla
- category: programming
- tags: python,pickle
- summary: Benchmark cPickle Python's module
- date: 2014-05-14 12:33:49

----------------

[`pickle`][1] is a standard library module to serialize and deserialize Python objects. Being written in pure Python, it's fairly slow, so the standard library provides a pure-C implementation, called [`cPickle`][2], with the limitation that it cannot be [subclassed][3].

What's interesting about `cPickle` are two little known settings that can speed up serialization quite substantially.

1. [`cPickle.HIGHEST_PROTOCOL`][4] basically dumps a Python object using a binary protocol, rather than the default ASCII-based, more portable, protocol 0. If portability or backward compatibility are not an issue for you, you should use it: it's documented and probably here to stay.

2. [`Pickler`][5]'s undocumented `fast` flag. It turns out that `cPickle` implementation has a "fast mode" that is enabled by setting this `fast` flag to `True`. It's undocumented so probably subject to change, but it makes dumping objects way faster.

Looking at the [implementation][6] of `cPickle`, the comments in the code have something to say about "fast mode":

> The fast mode disable the usage of memo,
> therefore speeding the pickling process by
> not generating superfluous PUT opcodes. It
> should not be used if with self-referential
> objects.

[memo][7] is basically a cache, within the pickler, that remembers what objects have already been processed, used mainly to avoid infinite loops when dumping self-referential data structures. But if you are dumping data structures that do not reference themselves, you can spare some time disabling this caching.

To test these settings, I compared "vanilla" `cPickle.dumps`, with "highest_protocol" and "fast mode", for 3 different objects: a small, a medium and a large list of dictionaries. The code is available in [`gist`][8]:

<script src="https://gist.github.com/lbolla/1bec1b70ef9c8e254b57.js"></script>

Clone it and run it:

	$> git clone https://gist.github.com/1bec1b70ef9c8e254b57.git pickle_experiments
	$> cd pickle_experiments
	$> sh run.sh

On my machine, I get these results:

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

_Note: I've reduced the number of iterations to 3 for "vanilla LARGE" because it was taking too long..._

"high_protocol" is between 2 and 3 times faster than "vanilla" for all objects, and **"fast mode" is 6 times faster than "high_protocol" and 10 times faster than "vanilla" for large objects**!


   [1]: https://docs.python.org/2/library/pickle.html
   [2]: https://docs.python.org/2/library/pickle.html#module-cPickle
   [3]: http://doughellmann.com/2007/06/24/pymotw-pickle-and-cpickle.html
   [4]: https://docs.python.org/2/library/pickle.html#pickle.HIGHEST_PROTOCOL
   [5]: https://docs.python.org/2/library/pickle.html#pickle.Pickler
   [6]: http://hg.python.org/cpython/file/c5464268aead/Modules/_pickle.c#l548
   [7]: https://docs.python.org/2/library/pickle.html#pickle.Pickler.clear_memo
   [8]: https://gist.github.com/lbolla/1bec1b70ef9c8e254b57
