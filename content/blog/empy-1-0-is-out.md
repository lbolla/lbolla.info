---
categories:
  - "programming"
date: "2015-04-26"
description: "EMpy 1.0 is out - Python3 compatible!"
tags:
  - "EMpy"
  - "python3"
title: "EMpy 1.0 is out! Python3 compatible!"
---

After a long sleep, I resumed development on [EMpy][1]. The trigger
was an appeal from Guido van Rossum at PyCon 2015 to package authors
to support Python 3.

There are no new features to EMpy, but I have:

  * ported the code to Python 3, using the amazing [future][2] library:
    now, both Python 2 and 3 are supported;
  * setup [Travis CI][3] to run unittest on all supported Python versions;
  * upgraded the dependencies to the latest available libraries;
  * Pylint'd and pep8'd the code
  * Renamed the package in PyPi to `ElectroMagneticPython` to avoid
    name conflicts with [EmPy][4].

You can try it out by simply:

    $> pip install ElectroMagneticPython

There is still to be done, to make EMpy "production ready", like
improving unittest coverage and documentation. If anyone is interested
to contribute, get in touch!

   [1]: http://lbolla.github.io/EMpy/
   [2]: http://python-future.org/
   [3]: https://travis-ci.org/lbolla/EMpy
   [4]: https://pypi.python.org/pypi/EmPy
