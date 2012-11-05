# MD5 vs SHA1 in Python

- author: lbolla
- category: programming
- tags: benchmark, python
- summary: Benchmark between `MD5` and `SHA1` in Python
- date: 2011-08-24 15:53:51

----------------

If you are interested to know if the [myth about `MD5` being faster than `SHA1`][1]
holds for Python, here is the result I got on my box:

    In [1]: import hashlib
    In [2]: %timeit hashlib.md5('text text text').hexdigest()
    1000000 loops, best of 3: 1.29 us per loop
    In [3]: %timeit hashlib.sha1('text text text').hexdigest()
    1000000 loops, best of 3: 1.4 us per loop

Result is: `MD5` is faster, but only just, in Python 2.7.2. Considering that [`MD5`
is broken][2], I think I'll use `SHA1`...

   [1]: http://omnifarious.livejournal.com/363945.html
   [2]: http://en.wikipedia.org/wiki/`MD5`
