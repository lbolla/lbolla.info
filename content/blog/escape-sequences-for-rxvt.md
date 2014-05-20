---
categories:
  - "programming"
date: "2009-05-01"
description: "None"
tags:
  - "X"
  - "vim"
  - "rxvt"
title: "Escape sequences for rxvt"
---

I'm posting this info because I had a hard time searching for it on the
internet.

If you are using `rxvt` (or `urxvt`), and you want escape sequences to work as
in `xterm`, you need to specify them in your `.Xdefaults`.

Here are the codes I had to add to have `vim` working properly on `rxvt` (I use
`alt-left_arrow` and `alt-right_arrow` to navigate through tabs):

    *Rxvt*meta8: false
    *Rxvt.keysym.C-Left: 033[1;5D
    *Rxvt.keysym.C-Right: 033[1;5C
    *Rxvt.keysym.M-Left: 033[1;3D
    *Rxvt.keysym.M-Right: 033[1;3C
