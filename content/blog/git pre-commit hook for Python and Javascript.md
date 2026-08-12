---
title: git pre-commit hook for Python and Javascript
date: 2011-11-17
tags:
- programming
- python
- javascript
---
Following a [recent discussion on HN](http://news.ycombinator.com/item?id=3244475), I decided to share my own [git pre-commit hook](http://book.git-scm.com/5_git_hooks.html).

``` python
#!/usr/bin/python

import os
import sys
import re
import subprocess


devnull = open(os.devnull, 'w')


def call(cmd):
    p = subprocess.Popen(cmd.split(),
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out.decode('utf-8'), err.decode('utf-8'), p.returncode


def execute(cmd, silent=False):
    if silent:
        params = {
                'stdout': devnull,
                'stderr': devnull,
                }
    else:
        params = {}

    retcode = subprocess.call(cmd.split(), **params)
    return retcode


def exists(cmd):
    return execute('which %s' % cmd, silent=True) == 0


def get_modified(ext):
    modified = re.compile('^(?:M|A).(?P<name>.*\.%s)' % ext)
    out, _, _ = call('git status --porcelain')
    modifieds = []
    for line in out.splitlines():
        match = modified.match(line.strip())
        if (match):
            modifieds.append(match.group('name'))
    return modifieds
```

It\'s a work-in-progress, so you can find the [most updated version here](https://github.com/lbolla/dotfiles/blob/master/githooks/pre-commit). To use it, just drop it in your `.git/hooks` directory. At every `git commit`, it will run `[pep8][4]` and `[pyflakes][5]` on `.py` files, and `[gjslint][6]` on `.js` files.
