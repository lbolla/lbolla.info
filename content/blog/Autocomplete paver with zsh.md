---
title: Autocomplete paver with zsh
date: 2014-09-14
---
Here is a quick way to have autocompletion of [paver](http://paver.github.io/paver/) tasks on [zsh](http://www.zsh.org/). Just add these lines to your `.zshrc` file:

```shell
_paver_tasks () {
    reply=( $(paver help | awk '/^  ([a-zA-Z_]+).+-/{print $1}') )
}
compctl -K _paver_tasks paver
```

Then, at a `zsh` prompt, if in a directory containing a `pavement.py` file, hitting `paver <TAB>` will list the available tasks.

Enjoy!
