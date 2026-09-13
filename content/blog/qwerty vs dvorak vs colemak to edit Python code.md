---
title: qwerty vs dvorak vs colemak to edit Python code
date: 2009-02-02
tags:
- programming
- python
---
Yesterday, I was intrigued by the idea of choosing a more efficient keyboard layout to work with everyday. As long as I type Python code 90% of my time, I decided to evaluate the efficiency of the first 3 most widespread keyboard layouts: [QWERTY](http://en.wikipedia.org/wiki/QWERTY), [Dvorak](http://en.wikipedia.org/wiki/Dvorak_Simplified_Keyboard) and [Colemak](http://en.wikipedia.org/wiki/Colemak). I used [this excellent tool](http://www.codeaxe.co.uk/dvorak/) to compare the three layouts over the first 50000 characters of the [webpy](http://webpy.org/) source code. Here are the results:

## Overall effort

| Layout  | Effort    | % improvement over worst layout |
| :------ | --------: | ------------------------------: |
| Qwerty  | 306,509.6 |                           0.0 % |
| Dvorak  | 283,868.7 |                           7.4 % |
| Colemak | 275,347.6 |                          10.2 % |


## Keys for each finger (stronger fingers should be used more often)

| Layout  | Thumbs | LPinky | LRing | LMiddle | LIndex | RIndex | RMiddle | RRing | RPinky | Total         |
| :------ | -----: | -----: | ----: | ------: | -----: | -----: | ------: | ----: | -----: | ------------: |
| Qwerty  | 25.9 % | 12.4 % | 5.3 % |   9.5 % | 11.6 % |  7.6 % |   5.6 % | 8.9 % | 13.2 % | 54,237.0 keys |
| Dvorak  | 25.9 % | 13.0 % | 5.2 % |   8.1 % |  7.3 % |  7.5 % |   7.5 % | 8.2 % | 17.3 % | 54,237.0 keys |
| Colemak | 25.9 % | 12.7 % | 4.8 % |   7.5 % |  9.5 % |  8.4 % |  10.1 % | 6.6 % | 14.5 % | 54,237.0 keys |

| Layout  | Thumbs | Left hand | Right hand | Total         |
| :------ | -----: | --------: | ---------: | ------------: |
| Qwerty  | 25.9 % |    38.8 % |     35.2 % | 54,237.0 keys |
| Dvorak  | 25.9 % |    33.6 % |     40.5 % | 54,237.0 keys |
| Colemak | 25.9 % |    34.5 % |     39.6 % | 54,237.0 keys |


## Finger Travel Distance (only the horizontal)

| Layout  | Thumbs | LPinky | LRing | LMiddle | LIndex | RIndex | RMiddle | RRing  | RPinky | Total     |
| :------ | -----: | -----: | ----: | ------: | -----: | -----: | ------: | -----: | -----: | --------: |
| Qwerty  |  0.0 % | 18.1 % | 2.0 % |  10.5 % | 15.5 % | 12.1 % |   8.6 % |  9.9 % | 23.4 % | 1,441.5 m |
| Dvorak  |  0.0 % | 21.1 % | 4.1 % |   3.5 % | 10.0 % | 12.5 % |   7.6 % | 10.8 % | 30.4 % | 1,210.3 m |
| Colemak |  0.0 % | 23.7 % | 2.5 % |   6.1 % | 10.2 % | 10.2 % |   9.3 % |  9.3 % | 28.6 % | 1,131.2 m |

| Layout  | Thumbs | Left hand | Right hand | Total     |
| :------ | -----: | --------: | ---------: | --------: |
| Qwerty  |  0.0 % |    46.0 % |     54.0 % | 1,441.5 m |
| Dvorak  |  0.0 % |    38.8 % |     61.2 % | 1,210.3 m |
| Colemak |  0.0 % |    42.6 % |     57.4 % | 1,131.2 m |


## % home keys (out of all character keys plus SHIFT and ENTER, but excluding keys operated by thumbs)

| Layout  | Percentage |
| :------ | ---------: |
| Qwerty  |     20.4 % |
| Dvorak  |     33.7 % |
| Colemak |     38.7 % |


## % keys typed with the same finger as the previous key (excluding repeating keys like ss)

| Layout  | Percentage |
| :------ | ---------: |
| Qwerty  |      4.5 % |
| Dvorak  |      3.8 % |
| Colemak |      3.6 % |


## % keys typed with the same hand as the previous key (ex: in Qwerty sd or ss are included, but s s is not since you type the space with the other hand)

| Layout  | Percentage |
| :------ | ---------: |
| Qwerty  |     26.8 % |
| Dvorak  |     20.0 % |
| Colemak |     24.6 % |


## % keys typed with the same hand as the previous key and jumping a row (ex: in Qwerty ev is a row jump -- you jump over the middle row -- and it's awkward to type; ef is not a row jump)

| Layout  | Percentage |
| :------ | ---------: |
| Qwerty  |     10.3 % |
| Dvorak  |      5.7 % |
| Colemak |      4.1 % |


## % keys typed with the same hand as the previous key and in reverse order (ex: in Qwerty df or kj are typed in the easier order pinky-ring-middle-index, whereas fd and jk are in reverse order index-middle-ring-pinky, and harder to type)

| Layout  | Percentage |
| :------ | ---------: |
| Qwerty  |     15.4 % |
| Dvorak  |     11.9 % |
| Colemak |     15.2 % |


## % keys that need the SHIFT modifier

| Layout  | Percentage |
| :------ | ---------: |
| Qwerty  |     14.3 % |
| Dvorak  |     14.3 % |
| Colemak |     14.3 % |


## Pairs of consecutive keys typed with the same finger in Qwerty

| Keys           | Frequency | Percentage |
| :------------- | --------: | ---------: |
| :/NewLine/     | 253 times |     0.47 % |
| de             | 200 times |     0.37 % |
| tr             | 158 times |     0.29 % |
| rt             | 102 times |     0.19 % |
| ol             |  99 times |     0.18 % |
| un             |  98 times |     0.18 % |
| q\_LeftShift\_ |  87 times |     0.16 % |
| ce             |  86 times |     0.16 % |
| “/NewLine/     |  81 times |     0.15 % |
| ed             |  80 times |     0.15 % |
| }/NewLine/     |  62 times |     0.11 % |


## Pairs of consecutive keys typed with the same finger in Dvorak

| Keys            | Frequency | Percentage |
| :-------------- | --------: | ---------: |
| ct              | 196 times |     0.36 % |
| s\_RightShift\_ | 169 times |     0.31 % |
| db              | 152 times |     0.28 % |
| l\_RightShift\_ | 137 times |     0.25 % |
| ‘/LeftShift/    | 133 times |     0.25 % |
| rn              | 115 times |     0.21 % |
| ls              | 100 times |     0.18 % |
| }/NewLine/      |  62 times |     0.11 % |
| =/RightShift/   |  59 times |     0.11 % |
| “/LeftShift/    |  58 times |     0.11 % |
| e.              |  58 times |     0.11 % |


## Pairs of consecutive keys typed with the same finger in Colemak

| Keys           | Frequency | Percentage |
| :------------- | --------: | ---------: |
| :/NewLine/     | 253 times |     0.47 % |
| ue             | 237 times |     0.44 % |
| db             | 152 times |     0.28 % |
| e,             |  89 times |     0.16 % |
| q\_LeftShift\_ |  87 times |     0.16 % |
| “/NewLine/     |  81 times |     0.15 % |
| }/NewLine/     |  62 times |     0.11 % |
| ]/NewLine/     |  46 times |     0.08 % |
| pt             |  44 times |     0.08 % |
| ‘/RightShift/  |  41 times |     0.08 % |
| “/RightShift/  |  41 times |     0.08 % |


## Key frequency in your text

| Key          | Frequency   | Percentage |
| :----------- | ----------: | ---------: |
| /Space/      | 14067 times |    25.94 % |
| /LeftShift/  |  4391 times |     8.10 % |
| e            |  3239 times |     5.97 % |
| t            |  2184 times |     4.03 % |
| s            |  2170 times |     4.00 % |
| r            |  1890 times |     3.48 % |
| a            |  1619 times |     2.99 % |
| o            |  1557 times |     2.87 % |
| l            |  1530 times |     2.82 % |
| n            |  1519 times |     2.80 % |
| /NewLine/    |  1511 times |     2.79 % |
| i            |  1372 times |     2.53 % |
| /RightShift/ |  1357 times |     2.50 % |
| d            |  1014 times |     1.87 % |
| f            |   971 times |     1.79 % |
| c            |   855 times |     1.58 % |
| u            |   851 times |     1.57 % |
| m            |   716 times |     1.32 % |
| p            |   715 times |     1.32 % |
| (            |   674 times |     1.24 % |
| )            |   673 times |     1.24 % |
| .            |   658 times |     1.21 % |
| ‘            |   623 times |     1.15 % |
| ,            |   573 times |     1.06 % |
| b            |   571 times |     1.05 % |
| “            |   563 times |     1.04 % |
| \_           |   554 times |     1.02 % |
| =            |   518 times |     0.96 % |
| :            |   490 times |     0.90 % |
| q            |   463 times |     0.85 % |
| y            |   423 times |     0.78 % |
| h            |   416 times |     0.77 % |
| w            |   352 times |     0.65 % |
| >            |   348 times |     0.64 % |
| g            |   304 times |     0.56 % |
| v            |   257 times |     0.47 % |
| x            |   253 times |     0.47 % |
| k            |   231 times |     0.43 % |
| <            |   154 times |     0.28 % |
| /            |   125 times |     0.23 % |
| []           |   119 times |     0.22 % |
| ;            |   113 times |     0.21 % |
| 0            |    86 times |     0.16 % |
| \`           |    85 times |     0.16 % |
| +            |    84 times |     0.15 % |
| 1            |    81 times |     0.15 % |
| {            |    80 times |     0.15 % |
| }            |    79 times |     0.15 % |
| -            |    78 times |     0.14 % |
| j            |    76 times |     0.14 % |
| *            |    72 times |     0.13 % |
| #            |    69 times |     0.13 % |
| 2            |    67 times |     0.12 % |
| %            |    55 times |     0.10 % |
| \$           |    52 times |     0.10 % |
| 3            |    31 times |     0.06 % |
| 6            |    29 times |     0.05 % |
| 8            |    18 times |     0.03 % |
| @            |    17 times |     0.03 % |
|              |    14 times |     0.03 % |
| z            |    13 times |     0.02 % |
| 5            |    13 times |     0.02 % |
| 4            |     8 times |     0.01 % |
| ?            |     8 times |     0.01 % |
| 9            |     7 times |     0.01 % |


## Frequent pairs of keys in your text

| Key Pair                | Frequency  | Percentage |
| :---------------------- | ---------: | ---------: |
| \_Space\_\_Space\_      | 9243 times |    17.04 % |
| \_NewLine\_\_Space\_    | 1233 times |     2.27 % |
| \_Space\_\_LeftShift\_  |  805 times |     1.48 % |
| /LeftShift/(            |  674 times |     1.24 % |
| /LeftShift/)            |  673 times |     1.24 % |
| /LeftShift/”            |  563 times |     1.04 % |
| \_LeftShift\_\_         |  554 times |     1.02 % |
| se                      |  549 times |     1.01 % |
| ,/Space/                |  543 times |     1.00 % |
| /LeftShift/:            |  490 times |     0.90 % |
| el                      |  405 times |     0.75 % |
| er                      |  377 times |     0.70 % |
| in                      |  364 times |     0.67 % |
| \_Space\_\_RightShift\_ |  362 times |     0.67 % |
| or                      |  352 times |     0.65 % |
| /LeftShift/>            |  348 times |     0.64 % |
| /Space/i                |  344 times |     0.63 % |
| /Space/s                |  341 times |     0.63 % |
| te                      |  340 times |     0.63 % |
| e\_LeftShift\_          |  338 times |     0.62 % |
| =/Space/                |  332 times |     0.61 % |
| /Space/=                |  321 times |     0.59 % |
| re                      |  306 times |     0.56 % |
| lf                      |  294 times |     0.54 % |
| )/NewLine/              |  281 times |     0.52 % |
| e\_Space\_              |  281 times |     0.52 % |

Actually, I was disappointed: there seem to be no clear advantage of Dvorak or Colemak, wrt QWERTY and, given the popularity of the latter, switching does not seem to be a good idea...
