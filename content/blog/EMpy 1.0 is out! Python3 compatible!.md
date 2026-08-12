---
title: EMpy 1.0 is out! Python3 compatible!
date: 2015-04-26
tags:
- programming
- python
---
After a long sleep, I resumed development on [Empy]({{< relref "blog/EMpy.md" >}}). The trigger was an appeal from Guido van Rossum at PyCon 2015 to package authors to support Python 3.

There are no new features to [Empy]({{< relref "blog/EMpy.md" >}}), but I have:

-   ported the code to Python 3, using the amazing [future](http://python-future.org/) library: now, both Python 2 and 3 are supported;
-   setup [Travis CI](https://travis-ci.org/lbolla/EMpy) to run unittest on all supported Python versions;
-   upgraded the dependencies to the latest available libraries;
-   Pylint\'d and pep8\'d the code
-   Renamed the package in PyPi to `ElectroMagneticPython` to avoid name conflicts with [EmPy](https://pypi.python.org/pypi/EmPy).

You can try it out by simply:

``` shell
$> pip install ElectroMagneticPython
```

There is still to be done, to make EMpy \"production ready\", like improving unittest coverage and documentation. If anyone is interested to contribute, get in touch!
