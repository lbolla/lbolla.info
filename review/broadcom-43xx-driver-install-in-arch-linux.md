# Broadcom 43xx driver install in Arch Linux

- title: Broadcom 43xx driver install in Arch Linux
- author: lbolla
- category: tech
- tags: 
- summary: 
- post_id: 429
- date: 2012-07-31 10:13:28
- post_date_gmt: 2012-07-31 09:13:28
- comment_status: open
- post_name: broadcom-43xx-driver-install-in-arch-linux
- status: publish
- post_type: post

----------------

This is a vintage post to remind me how to install b43 drivers on Arch Linux for my "shiny" Belkin PCMCIA card (dated 2002...) First install the firmware extractor: `$> pacman -S b43-fwcutter` Then install the firmware itself: `$> yaourt -S b43-firmware` Check `dmesg`. You should see something like: 

> Broadcom 43xx driver loaded [ Features: PMNLS ]

and `lsmod | grep b43`: 

> b43 330774 0 bcma 19281 1 b43 mac80211 341044 1 b43 cfg80211 147429 2 b43,mac80211 ssb 42167 2 b43,b44 pcmcia 31182 2 b43,ssb mmc_core 72742 2 b43,ssb

Finally, try to connect: `$> pacman -S wifi-select` `$> wifi-select`