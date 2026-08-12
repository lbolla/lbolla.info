---
title: hsenv
date: 2012-03-29
tags:
- programming
- python
- haskell
---
If you have never used [hsenv](https://github.com/Paczesiowa/hsenv) before, you should. It\'s basically the Haskell\'s equivalent of Python\'s [virtualenv](http://pypi.python.org/pypi/virtualenv).

You can find a [tweaked version of hsenv here](https://github.com/lbolla/hsenv): I\'ve relaxed some requirements in order to make it install on newer GHC releases.

Finally, if when using you hit this error:

``` shell
$ hsenv Creating Virtual Haskell directory structure
Installing GHC Initializing GHC Package database at /home/lollo/work/Unique/.hsenv/ghc_pkg_db
Copying necessary packages from original GHC package database
hsenv: fd:9: hGetContents: invalid argument (invalid byte sequence)
hsenv: thread blocked indefinitely in an MVar operation
```

Then, you have a problem with your locale. Follow the steps [here](https://wiki.archlinux.org/index.php/Locale#Enabling_necessary_locales), and retry.
