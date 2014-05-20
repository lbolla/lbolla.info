---
categories:
  - "tech"
date: "2012-07-31"
description: "How to install Broadcom drivers in Linux"
tags:
  - "linux"
  - "wireless"
title: "Broadcom 43xx driver install in Arch Linux"
---

This is a vintage post to remind me how to install `b43` drivers on Arch Linux for my "shiny" Belkin PCMCIA card (dated 2002...).

* First install the firmware extractor: `$> pacman -S b43-fwcutter`.
* Then install the firmware itself: `$> yaourt -S b43-firmware`.

Check `dmesg`. You should see something like: 

> Broadcom 43xx driver loaded [ Features: PMNLS ]

and `lsmod | grep b43`: 

> b43 330774 0 bcma 19281 1 b43 mac80211 341044 1 b43 cfg80211 147429 2 b43,mac80211 ssb 42167 2 b43,b44 pcmcia 31182 2 b43,ssb mmc_core 72742 2 b43,ssb

Finally, try to connect:

    $> pacman -S wifi-select
    $> wifi-select
