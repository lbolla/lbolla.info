---
categories:
  - "programming"
date: "2014-09-14"
description: "How to setup zsh so that it autocompletes paver"
tags:
  - "paver"
  - "zsh"
title: "Autocomplete paver with zsh"
---

Here is a quick way to have autocompletion of [paver][1] tasks on [zsh][2]. Just add these lines to your `.zshrc` file:

	_paver_tasks () {
		reply=( $(paver help | awk '/^  ([a-zA-Z_]+).+-/{print $1}') )
	}
	compctl -K _paver_tasks paver

Then, at a `zsh` prompt, if in a directory containing a `pavement.py` file, hitting `paver <TAB>` will list the available tasks.

Enjoy!

   [1]: http://paver.github.io/paver/
   [2]: http://www.zsh.org/
