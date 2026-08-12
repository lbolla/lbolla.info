---
title: Editors speed on opening big files
date: 2010-05-17
tags:
- programming
---
While playing with different editors (namely [vim](http://www.vim.org) and [sam](http://sam.cat-v.org/)) I tried to time how long some common editors take to open a big file (\~140Mb).

Then, for curiosity, I timed `less` with and without (`-n`) line numbering:

Here are the results:


|editor     | real    | user | sys |
| --- | --- | --- | --- |
| `ed`| 4.866s| 3.440s| 3.440s |
|`vim` |2.086s |0.836s | 0.232s |
|`nano` |16.264s |15.361s |0.172s |
|`sam` |way too long | | |
|`less` |3.552s |0.200s |0.072s |
|`less -n` | 0.182s |0.016s |0.016s |

Not sure what to do with these numbers, yet...
