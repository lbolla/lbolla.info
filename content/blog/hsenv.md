# hsenv

- author: lbolla
- category: programming
- tags: haskell
- summary: Virtual environment for Haskell
- date: 2012-03-29 11:04:55

----------------

If you have never used [hsenv][1] before, you should. It's basically the
Haskell's equivalent of Python's [virtualenv][2].

You can find a [tweaked version of hsenv here][3]: I've relaxed some
requirements in order to make it install on newer GHC releases.

Finally, if when using you hit this error:

    $ hsenv Creating Virtual Haskell directory structure
    Installing GHC Initializing GHC Package database at /home/lollo/work/Unique/.hsenv/ghc_pkg_db
    Copying necessary packages from original GHC package database
    hsenv: fd:9: hGetContents: invalid argument (invalid byte sequence)
    hsenv: thread blocked indefinitely in an MVar operation

Then, you have a problem with your locale. Follow the steps [here][4],
and retry.

   [1]: https://github.com/Paczesiowa/hsenv
   [2]: http://pypi.python.org/pypi/virtualenv
   [3]: https://github.com/lbolla/hsenv
   [4]: https://wiki.archlinux.org/index.php/Locale#Enabling_necessary_locales
