---
categories:
  - "programming"
date: "2009-02-02"
tags:
  - "python"
title: "qwerty vs dvorak vs colemak to edit Python code"
---

Yesterday, I was intrigued by the idea of choosing a more efficient keyboard
layout to work with everyday. As long as I type Python code 90% of my time, I
decided to evaluate the efficiency of the first 3 most widespread keyboard
layouts: [QWERTY][1], [Dvorak][2] and [Colemak][3]. I used [this excellent
tool][4] to compare the three layouts over the first 50000 characters of the
[webpy][5] source code. Here are the results: 

<div id="page">
<div id="text">
<h1>The Qwerty Keyboard Layout Vs The Dvorak Keyboard Layout</h1>
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>Overall effort</h2>
<table>
<thead class="small">
<tr>
<td class="a1">Layout</td>
<td class="a0">Effort</td>
<td class="a1">% improvement over worst layout</td>
<td class="a0"></td>
</tr>
</thead>
<tbody>
<tr>
<td class="a1"><strong>Qwerty</strong></td>
<td class="a0" style="text-align: right;">306,509.6</td>
<td class="a1" style="text-align: right;">0.0 %</td>
<td class="a0"></td>
</tr>
<tr>
<td class="a1"><strong>Dvorak</strong></td>
<td class="a0" style="text-align: right;">283,868.7</td>
<td class="a1" style="text-align: right;">7.4 %</td>
<td class="a0"></td>
</tr>
<tr>
<td class="a1"><strong>Colemak</strong></td>
<td class="a0" style="text-align: right;">275,347.6</td>
<td class="a1" style="text-align: right;">10.2 %</td>
<td class="a0"></td>
</tr>
</tbody>
</table>
<hr />
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>Keys for each finger
(stronger fingers should be used more often)</h2>
<table>
<thead class="small">
<tr>
<td class="a1">Layout</td>
<td class="a0">Thumbs</td>
<td class="a1">LPinky</td>
<td class="a0">LRing</td>
<td class="a1">LMiddle</td>
<td class="a0">LIndex</td>
<td class="a1">RIndex</td>
<td class="a0">RMiddle</td>
<td class="a1">RRing</td>
<td class="a0">RPinky</td>
<td class="a1">Total</td>
</tr>
</thead>
<tbody>
<tr>
<td class="a1"><strong>Qwerty</strong></td>
<td class="a0" style="text-align: right;">25.9 %</td>
<td class="a1" style="text-align: right;">12.4 %</td>
<td class="a0" style="text-align: right;">5.3 %</td>
<td class="a1" style="text-align: right;">9.5 %</td>
<td class="a0" style="text-align: right;">11.6 %</td>
<td class="a1" style="text-align: right;">7.6 %</td>
<td class="a0" style="text-align: right;">5.6 %</td>
<td class="a1" style="text-align: right;">8.9 %</td>
<td class="a0" style="text-align: right;">13.2 %</td>
<td class="a1" style="text-align: right;">54,237.0 keys</td>
</tr>
<tr>
<td class="a1"><strong>Dvorak</strong></td>
<td class="a0" style="text-align: right;">25.9 %</td>
<td class="a1" style="text-align: right;">13.0 %</td>
<td class="a0" style="text-align: right;">5.2 %</td>
<td class="a1" style="text-align: right;">8.1 %</td>
<td class="a0" style="text-align: right;">7.3 %</td>
<td class="a1" style="text-align: right;">7.5 %</td>
<td class="a0" style="text-align: right;">7.5 %</td>
<td class="a1" style="text-align: right;">8.2 %</td>
<td class="a0" style="text-align: right;">17.3 %</td>
<td class="a1" style="text-align: right;">54,237.0 keys</td>
</tr>
<tr>
<td class="a1"><strong>Colemak</strong></td>
<td class="a0" style="text-align: right;">25.9 %</td>
<td class="a1" style="text-align: right;">12.7 %</td>
<td class="a0" style="text-align: right;">4.8 %</td>
<td class="a1" style="text-align: right;">7.5 %</td>
<td class="a0" style="text-align: right;">9.5 %</td>
<td class="a1" style="text-align: right;">8.4 %</td>
<td class="a0" style="text-align: right;">10.1 %</td>
<td class="a1" style="text-align: right;">6.6 %</td>
<td class="a0" style="text-align: right;">14.5 %</td>
<td class="a1" style="text-align: right;">54,237.0 keys</td>
</tr>
</tbody>
</table>
<table>
<thead class="small">
<tr>
<td class="a1">Layout</td>
<td class="a0">Thumbs</td>
<td class="a1">Left hand</td>
<td class="a0">Right hand</td>
<td class="a1">Total</td>
<td class="a0"></td>
</tr>
</thead>
<tbody>
<tr>
<td class="a1"><strong>Qwerty</strong></td>
<td class="a0" style="text-align: right;">25.9 %</td>
<td class="a1" style="text-align: right;">38.8 %</td>
<td class="a0" style="text-align: right;">35.2 %</td>
<td class="a1" style="text-align: right;">54,237.0 keys</td>
<td class="a0"></td>
</tr>
<tr>
<td class="a1"><strong>Dvorak</strong></td>
<td class="a0" style="text-align: right;">25.9 %</td>
<td class="a1" style="text-align: right;">33.6 %</td>
<td class="a0" style="text-align: right;">40.5 %</td>
<td class="a1" style="text-align: right;">54,237.0 keys</td>
<td class="a0"></td>
</tr>
<tr>
<td class="a1"><strong>Colemak</strong></td>
<td class="a0" style="text-align: right;">25.9 %</td>
<td class="a1" style="text-align: right;">34.5 %</td>
<td class="a0" style="text-align: right;">39.6 %</td>
<td class="a1" style="text-align: right;">54,237.0 keys</td>
<td class="a0"></td>
</tr>
</tbody>
</table>
<hr />
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>Finger Travel
Distance (only the horizontal)</h2>
<table>
<thead class="small">
<tr>
<td class="a1">Layout</td>
<td class="a0">Thumbs</td>
<td class="a1">LPinky</td>
<td class="a0">LRing</td>
<td class="a1">LMiddle</td>
<td class="a0">LIndex</td>
<td class="a1">RIndex</td>
<td class="a0">RMiddle</td>
<td class="a1">RRing</td>
<td class="a0">RPinky</td>
<td class="a1">Total</td>
</tr>
</thead>
<tbody>
<tr>
<td class="a1"><strong>Qwerty</strong></td>
<td class="a0" style="text-align: right;">0.0 %</td>
<td class="a1" style="text-align: right;">18.1 %</td>
<td class="a0" style="text-align: right;">2.0 %</td>
<td class="a1" style="text-align: right;">10.5 %</td>
<td class="a0" style="text-align: right;">15.5 %</td>
<td class="a1" style="text-align: right;">12.1 %</td>
<td class="a0" style="text-align: right;">8.6 %</td>
<td class="a1" style="text-align: right;">9.9 %</td>
<td class="a0" style="text-align: right;">23.4 %</td>
<td class="a1" style="text-align: right;">1,441.5 m</td>
</tr>
<tr>
<td class="a1"><strong>Dvorak</strong></td>
<td class="a0" style="text-align: right;">0.0 %</td>
<td class="a1" style="text-align: right;">21.1 %</td>
<td class="a0" style="text-align: right;">4.1 %</td>
<td class="a1" style="text-align: right;">3.5 %</td>
<td class="a0" style="text-align: right;">10.0 %</td>
<td class="a1" style="text-align: right;">12.5 %</td>
<td class="a0" style="text-align: right;">7.6 %</td>
<td class="a1" style="text-align: right;">10.8 %</td>
<td class="a0" style="text-align: right;">30.4 %</td>
<td class="a1" style="text-align: right;">1,210.3 m</td>
</tr>
<tr>
<td class="a1"><strong>Colemak</strong></td>
<td class="a0" style="text-align: right;">0.0 %</td>
<td class="a1" style="text-align: right;">23.7 %</td>
<td class="a0" style="text-align: right;">2.5 %</td>
<td class="a1" style="text-align: right;">6.1 %</td>
<td class="a0" style="text-align: right;">10.2 %</td>
<td class="a1" style="text-align: right;">10.2 %</td>
<td class="a0" style="text-align: right;">9.3 %</td>
<td class="a1" style="text-align: right;">9.3 %</td>
<td class="a0" style="text-align: right;">28.6 %</td>
<td class="a1" style="text-align: right;">1,131.2 m</td>
</tr>
</tbody>
</table>
<table>
<thead class="small">
<tr>
<td class="a1">Layout</td>
<td class="a0">Thumbs</td>
<td class="a1">Left hand</td>
<td class="a0">Right hand</td>
<td class="a1">Total</td>
<td class="a0"></td>
</tr>
</thead>
<tbody>
<tr>
<td class="a1"><strong>Qwerty</strong></td>
<td class="a0" style="text-align: right;">0.0 %</td>
<td class="a1" style="text-align: right;">46.0 %</td>
<td class="a0" style="text-align: right;">54.0 %</td>
<td class="a1" style="text-align: right;">1,441.5 m</td>
<td class="a0"></td>
</tr>
<tr>
<td class="a1"><strong>Dvorak</strong></td>
<td class="a0" style="text-align: right;">0.0 %</td>
<td class="a1" style="text-align: right;">38.8 %</td>
<td class="a0" style="text-align: right;">61.2 %</td>
<td class="a1" style="text-align: right;">1,210.3 m</td>
<td class="a0"></td>
</tr>
<tr>
<td class="a1"><strong>Colemak</strong></td>
<td class="a0" style="text-align: right;">0.0 %</td>
<td class="a1" style="text-align: right;">42.6 %</td>
<td class="a0" style="text-align: right;">57.4 %</td>
<td class="a1" style="text-align: right;">1,131.2 m</td>
<td class="a0"></td>
</tr>
</tbody>
</table>
<hr />
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>% home keys (out of
all character keys plus <tt>SHIFT</tt> and <tt>ENTER</tt>, but excluding keys
operated by thumbs)</h2>
<table>
<tbody>
<tr>
<td><strong>Qwerty</strong></td>
<td style="text-align: right;"><strong>20.4 %</strong></td>
<td class="bar"></td>
</tr>
<tr>
<td><strong>Dvorak</strong></td>
<td style="text-align: right;"><strong>33.7 %</strong></td>
<td class="bar"></td>
</tr>
<tr>
<td><strong>Colemak</strong></td>
<td style="text-align: right;"><strong>38.7 %</strong></td>
<td class="bar"></td>
</tr>
</tbody>
</table>
<hr />
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>% keys typed with
the same finger as the previous key (excluding repeating keys like
<tt>ss</tt>)</h2>
<table>
<tbody>
<tr>
<td><strong>Qwerty</strong></td>
<td style="text-align: right;"><strong>4.5 %</strong></td>
<td class="bar"></td>
</tr>
<tr>
<td><strong>Dvorak</strong></td>
<td style="text-align: right;"><strong>3.8 %</strong></td>
<td class="bar"></td>
</tr>
<tr>
<td><strong>Colemak</strong></td>
<td style="text-align: right;"><strong>3.6 %</strong></td>
<td class="bar"></td>
</tr>
</tbody>
</table>
<hr />
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>% keys typed with
the same hand as the previous key (ex: in Qwerty <tt>sd</tt> or <tt>ss</tt> are
included, but <tt>s s</tt> is not since you type the space with the other
hand)</h2>
<table>
<tbody>
<tr>
<td><strong>Qwerty</strong></td>
<td style="text-align: right;"><strong>26.8 %</strong></td>
<td class="bar"></td>
</tr>
<tr>
<td><strong>Dvorak</strong></td>
<td style="text-align: right;"><strong>20.0 %</strong></td>
<td class="bar"></td>
</tr>
<tr>
<td><strong>Colemak</strong></td>
<td style="text-align: right;"><strong>24.6 %</strong></td>
<td class="bar"></td>
</tr>
</tbody>
</table>
<hr />
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>% keys typed with
the same hand as the previous key and jumping a row (ex: in Qwerty <tt>ev</tt>
is a row jump &#8211; you jump over the middle row &#8211; and it&#8217;s
awkward to type; <tt>ef</tt> is not a row jump)</h2>
<table>
<tbody>
<tr>
<td><strong>Qwerty</strong></td>
<td style="text-align: right;"><strong>10.3 %</strong></td>
<td class="bar"></td>
</tr>
<tr>
<td><strong>Dvorak</strong></td>
<td style="text-align: right;"><strong>5.7 %</strong></td>
<td class="bar"></td>
</tr>
<tr>
<td><strong>Colemak</strong></td>
<td style="text-align: right;"><strong>4.1 %</strong></td>
<td class="bar"></td>
</tr>
</tbody>
</table>
<hr />
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>% keys typed with
the same hand as the previous key and in reverse order (ex: in Qwerty
<tt>df</tt> or <tt>kj</tt> are typed in the easier order
pinky-ring-middle-index, whereas <tt>fd</tt> and <tt>jk</tt> are in reverse
order index-middle-ring-pinky, and harder to type)</h2>
<table>
<tbody>
<tr>
<td><strong>Qwerty</strong></td>
<td style="text-align: right;"><strong>15.4 %</strong></td>
<td class="bar"></td>
</tr>
<tr>
<td><strong>Dvorak</strong></td>
<td style="text-align: right;"><strong>11.9 %</strong></td>
<td class="bar"></td>
</tr>
<tr>
<td><strong>Colemak</strong></td>
<td style="text-align: right;"><strong>15.2 %</strong></td>
<td class="bar"></td>
</tr>
</tbody>
</table>
<hr />
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>% keys that need the
SHIFT modifier</h2>
<table>
<tbody>
<tr>
<td><strong>Qwerty</strong></td>
<td style="text-align: right;"><strong>14.3 %</strong></td>
<td class="bar"></td>
</tr>
<tr>
<td><strong>Dvorak</strong></td>
<td style="text-align: right;"><strong>14.3 %</strong></td>
<td class="bar"></td>
</tr>
<tr>
<td><strong>Colemak</strong></td>
<td style="text-align: right;"><strong>14.3 %</strong></td>
<td class="bar"></td>
</tr>
</tbody>
</table>
<hr />
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>Pairs of consecutive
keys typed with the same finger in Qwerty</h2>
<table>
<tbody>
<tr>
<td>:_NewLine_</td>
<td style="text-align: right;"><tt>253 times</tt></td>
<td style="text-align: right;">0.47 %</td>
</tr>
<tr>
<td>de</td>
<td style="text-align: right;"><tt>200 times</tt></td>
<td style="text-align: right;">0.37 %</td>
</tr>
<tr>
<td>tr</td>
<td style="text-align: right;"><tt>158 times</tt></td>
<td style="text-align: right;">0.29 %</td>
</tr>
<tr>
<td>rt</td>
<td style="text-align: right;"><tt>102 times</tt></td>
<td style="text-align: right;">0.19 %</td>
</tr>
<tr>
<td>ol</td>
<td style="text-align: right;"><tt>99 times</tt></td>
<td style="text-align: right;">0.18 %</td>
</tr>
<tr>
<td>un</td>
<td style="text-align: right;"><tt>98 times</tt></td>
<td style="text-align: right;">0.18 %</td>
</tr>
<tr>
<td>q_LeftShift_</td>
<td style="text-align: right;"><tt>87 times</tt></td>
<td style="text-align: right;">0.16 %</td>
</tr>
<tr>
<td>ce</td>
<td style="text-align: right;"><tt>86 times</tt></td>
<td style="text-align: right;">0.16 %</td>
</tr>
<tr>
<td>&#8220;_NewLine_</td>
<td style="text-align: right;"><tt>81 times</tt></td>
<td style="text-align: right;">0.15 %</td>
</tr>
<tr>
<td>ed</td>
<td style="text-align: right;"><tt>80 times</tt></td>
<td style="text-align: right;">0.15 %</td>
</tr>
<tr>
<td>}_NewLine_</td>
<td style="text-align: right;"><tt>62 times</tt></td>
<td style="text-align: right;">0.11 %</td>
</tr>
</tbody>
</table>
<hr />
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>Pairs of consecutive
keys typed with the same finger in Dvorak</h2>
<table>
<tbody>
<tr>
<td>ct</td>
<td style="text-align: right;"><tt>196 times</tt></td>
<td style="text-align: right;">0.36 %</td>
</tr>
<tr>
<td>s_RightShift_</td>
<td style="text-align: right;"><tt>169 times</tt></td>
<td style="text-align: right;">0.31 %</td>
</tr>
<tr>
<td>db</td>
<td style="text-align: right;"><tt>152 times</tt></td>
<td style="text-align: right;">0.28 %</td>
</tr>
<tr>
<td>l_RightShift_</td>
<td style="text-align: right;"><tt>137 times</tt></td>
<td style="text-align: right;">0.25 %</td>
</tr>
<tr>
<td>&#8216;_LeftShift_</td>
<td style="text-align: right;"><tt>133 times</tt></td>
<td style="text-align: right;">0.25 %</td>
</tr>
<tr>
<td>rn</td>
<td style="text-align: right;"><tt>115 times</tt></td>
<td style="text-align: right;">0.21 %</td>
</tr>
<tr>
<td>ls</td>
<td style="text-align: right;"><tt>100 times</tt></td>
<td style="text-align: right;">0.18 %</td>
</tr>
<tr>
<td>}_NewLine_</td>
<td style="text-align: right;"><tt>62 times</tt></td>
<td style="text-align: right;">0.11 %</td>
</tr>
<tr>
<td>=_RightShift_</td>
<td style="text-align: right;"><tt>59 times</tt></td>
<td style="text-align: right;">0.11 %</td>
</tr>
<tr>
<td>&#8220;_LeftShift_</td>
<td style="text-align: right;"><tt>58 times</tt></td>
<td style="text-align: right;">0.11 %</td>
</tr>
<tr>
<td>e.</td>
<td style="text-align: right;"><tt>58 times</tt></td>
<td style="text-align: right;">0.11 %</td>
</tr>
</tbody>
</table>
<hr />
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>Pairs of consecutive
keys typed with the same finger in Colemak</h2>
<table>
<tbody>
<tr>
<td>:_NewLine_</td>
<td style="text-align: right;"><tt>253 times</tt></td>
<td style="text-align: right;">0.47 %</td>
</tr>
<tr>
<td>ue</td>
<td style="text-align: right;"><tt>237 times</tt></td>
<td style="text-align: right;">0.44 %</td>
</tr>
<tr>
<td>db</td>
<td style="text-align: right;"><tt>152 times</tt></td>
<td style="text-align: right;">0.28 %</td>
</tr>
<tr>
<td>e,</td>
<td style="text-align: right;"><tt>89 times</tt></td>
<td style="text-align: right;">0.16 %</td>
</tr>
<tr>
<td>q_LeftShift_</td>
<td style="text-align: right;"><tt>87 times</tt></td>
<td style="text-align: right;">0.16 %</td>
</tr>
<tr>
<td>&#8220;_NewLine_</td>
<td style="text-align: right;"><tt>81 times</tt></td>
<td style="text-align: right;">0.15 %</td>
</tr>
<tr>
<td>}_NewLine_</td>
<td style="text-align: right;"><tt>62 times</tt></td>
<td style="text-align: right;">0.11 %</td>
</tr>
<tr>
<td>]_NewLine_</td>
<td style="text-align: right;"><tt>46 times</tt></td>
<td style="text-align: right;">0.08 %</td>
</tr>
<tr>
<td>pt</td>
<td style="text-align: right;"><tt>44 times</tt></td>
<td style="text-align: right;">0.08 %</td>
</tr>
<tr>
<td>&#8216;_RightShift_</td>
<td style="text-align: right;"><tt>41 times</tt></td>
<td style="text-align: right;">0.08 %</td>
</tr>
<tr>
<td>&#8220;_RightShift_</td>
<td style="text-align: right;"><tt>41 times</tt></td>
<td style="text-align: right;">0.08 %</td>
</tr>
</tbody>
</table>
<hr />
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>Key frequency in
your text</h2>
<table>
<tbody>
<tr>
<td>_Space_</td>
<td style="text-align: right;"><tt>14067 times</tt></td>
<td style="text-align: right;">25.94 %</td>
</tr>
<tr>
<td>_LeftShift_</td>
<td style="text-align: right;"><tt>4391 times</tt></td>
<td style="text-align: right;">8.10 %</td>
</tr>
<tr>
<td>e</td>
<td style="text-align: right;"><tt>3239 times</tt></td>
<td style="text-align: right;">5.97 %</td>
</tr>
<tr>
<td>t</td>
<td style="text-align: right;"><tt>2184 times</tt></td>
<td style="text-align: right;">4.03 %</td>
</tr>
<tr>
<td>s</td>
<td style="text-align: right;"><tt>2170 times</tt></td>
<td style="text-align: right;">4.00 %</td>
</tr>
<tr>
<td>r</td>
<td style="text-align: right;"><tt>1890 times</tt></td>
<td style="text-align: right;">3.48 %</td>
</tr>
<tr>
<td>a</td>
<td style="text-align: right;"><tt>1619 times</tt></td>
<td style="text-align: right;">2.99 %</td>
</tr>
<tr>
<td>o</td>
<td style="text-align: right;"><tt>1557 times</tt></td>
<td style="text-align: right;">2.87 %</td>
</tr>
<tr>
<td>l</td>
<td style="text-align: right;"><tt>1530 times</tt></td>
<td style="text-align: right;">2.82 %</td>
</tr>
<tr>
<td>n</td>
<td style="text-align: right;"><tt>1519 times</tt></td>
<td style="text-align: right;">2.80 %</td>
</tr>
<tr>
<td>_NewLine_</td>
<td style="text-align: right;"><tt>1511 times</tt></td>
<td style="text-align: right;">2.79 %</td>
</tr>
<tr>
<td>i</td>
<td style="text-align: right;"><tt>1372 times</tt></td>
<td style="text-align: right;">2.53 %</td>
</tr>
<tr>
<td>_RightShift_</td>
<td style="text-align: right;"><tt>1357 times</tt></td>
<td style="text-align: right;">2.50 %</td>
</tr>
<tr>
<td>d</td>
<td style="text-align: right;"><tt>1014 times</tt></td>
<td style="text-align: right;">1.87 %</td>
</tr>
<tr>
<td>f</td>
<td style="text-align: right;"><tt>971 times</tt></td>
<td style="text-align: right;">1.79 %</td>
</tr>
<tr>
<td>c</td>
<td style="text-align: right;"><tt>855 times</tt></td>
<td style="text-align: right;">1.58 %</td>
</tr>
<tr>
<td>u</td>
<td style="text-align: right;"><tt>851 times</tt></td>
<td style="text-align: right;">1.57 %</td>
</tr>
<tr>
<td>m</td>
<td style="text-align: right;"><tt>716 times</tt></td>
<td style="text-align: right;">1.32 %</td>
</tr>
<tr>
<td>p</td>
<td style="text-align: right;"><tt>715 times</tt></td>
<td style="text-align: right;">1.32 %</td>
</tr>
<tr>
<td>(</td>
<td style="text-align: right;"><tt>674 times</tt></td>
<td style="text-align: right;">1.24 %</td>
</tr>
<tr>
<td>)</td>
<td style="text-align: right;"><tt>673 times</tt></td>
<td style="text-align: right;">1.24 %</td>
</tr>
<tr>
<td>.</td>
<td style="text-align: right;"><tt>658 times</tt></td>
<td style="text-align: right;">1.21 %</td>
</tr>
<tr>
<td>&#8216;</td>
<td style="text-align: right;"><tt>623 times</tt></td>
<td style="text-align: right;">1.15 %</td>
</tr>
<tr>
<td>,</td>
<td style="text-align: right;"><tt>573 times</tt></td>
<td style="text-align: right;">1.06 %</td>
</tr>
<tr>
<td>b</td>
<td style="text-align: right;"><tt>571 times</tt></td>
<td style="text-align: right;">1.05 %</td>
</tr>
<tr>
<td>&#8220;</td>
<td style="text-align: right;"><tt>563 times</tt></td>
<td style="text-align: right;">1.04 %</td>
</tr>
<tr>
<td>_</td>
<td style="text-align: right;"><tt>554 times</tt></td>
<td style="text-align: right;">1.02 %</td>
</tr>
<tr>
<td>=</td>
<td style="text-align: right;"><tt>518 times</tt></td>
<td style="text-align: right;">0.96 %</td>
</tr>
<tr>
<td>:</td>
<td style="text-align: right;"><tt>490 times</tt></td>
<td style="text-align: right;">0.90 %</td>
</tr>
<tr>
<td>q</td>
<td style="text-align: right;"><tt>463 times</tt></td>
<td style="text-align: right;">0.85 %</td>
</tr>
<tr>
<td>y</td>
<td style="text-align: right;"><tt>423 times</tt></td>
<td style="text-align: right;">0.78 %</td>
</tr>
<tr>
<td>h</td>
<td style="text-align: right;"><tt>416 times</tt></td>
<td style="text-align: right;">0.77 %</td>
</tr>
<tr>
<td>w</td>
<td style="text-align: right;"><tt>352 times</tt></td>
<td style="text-align: right;">0.65 %</td>
</tr>
<tr>
<td>&gt;</td>
<td style="text-align: right;"><tt>348 times</tt></td>
<td style="text-align: right;">0.64 %</td>
</tr>
<tr>
<td>g</td>
<td style="text-align: right;"><tt>304 times</tt></td>
<td style="text-align: right;">0.56 %</td>
</tr>
<tr>
<td>v</td>
<td style="text-align: right;"><tt>257 times</tt></td>
<td style="text-align: right;">0.47 %</td>
</tr>
<tr>
<td>x</td>
<td style="text-align: right;"><tt>253 times</tt></td>
<td style="text-align: right;">0.47 %</td>
</tr>
<tr>
<td>k</td>
<td style="text-align: right;"><tt>231 times</tt></td>
<td style="text-align: right;">0.43 %</td>
</tr>
<tr>
<td>&lt;</td>
<td style="text-align: right;"><tt>154 times</tt></td>
<td style="text-align: right;">0.28 %</td>
</tr>
<tr>
<td>/</td>
<td style="text-align: right;"><tt>125 times</tt></td>
<td style="text-align: right;">0.23 %</td>
</tr>
<tr>
<td>[</td>
<td style="text-align: right;"><tt>120 times</tt></td>
<td style="text-align: right;">0.22 %</td>
</tr>
<tr>
<td>]</td>
<td style="text-align: right;"><tt>119 times</tt></td>
<td style="text-align: right;">0.22 %</td>
</tr>
<tr>
<td>;</td>
<td style="text-align: right;"><tt>113 times</tt></td>
<td style="text-align: right;">0.21 %</td>
</tr>
<tr>
<td>0</td>
<td style="text-align: right;"><tt>86 times</tt></td>
<td style="text-align: right;">0.16 %</td>
</tr>
<tr>
<td>`</td>
<td style="text-align: right;"><tt>85 times</tt></td>
<td style="text-align: right;">0.16 %</td>
</tr>
<tr>
<td>+</td>
<td style="text-align: right;"><tt>84 times</tt></td>
<td style="text-align: right;">0.15 %</td>
</tr>
<tr>
<td>1</td>
<td style="text-align: right;"><tt>81 times</tt></td>
<td style="text-align: right;">0.15 %</td>
</tr>
<tr>
<td>{</td>
<td style="text-align: right;"><tt>80 times</tt></td>
<td style="text-align: right;">0.15 %</td>
</tr>
<tr>
<td>}</td>
<td style="text-align: right;"><tt>79 times</tt></td>
<td style="text-align: right;">0.15 %</td>
</tr>
<tr>
<td>-</td>
<td style="text-align: right;"><tt>78 times</tt></td>
<td style="text-align: right;">0.14 %</td>
</tr>
<tr>
<td>j</td>
<td style="text-align: right;"><tt>76 times</tt></td>
<td style="text-align: right;">0.14 %</td>
</tr>
<tr>
<td>*</td>
<td style="text-align: right;"><tt>72 times</tt></td>
<td style="text-align: right;">0.13 %</td>
</tr>
<tr>
<td>#</td>
<td style="text-align: right;"><tt>69 times</tt></td>
<td style="text-align: right;">0.13 %</td>
</tr>
<tr>
<td>2</td>
<td style="text-align: right;"><tt>67 times</tt></td>
<td style="text-align: right;">0.12 %</td>
</tr>
<tr>
<td>%</td>
<td style="text-align: right;"><tt>55 times</tt></td>
<td style="text-align: right;">0.10 %</td>
</tr>
<tr>
<td>$</td>
<td style="text-align: right;"><tt>52 times</tt></td>
<td style="text-align: right;">0.10 %</td>
</tr>
<tr>
<td>3</td>
<td style="text-align: right;"><tt>31 times</tt></td>
<td style="text-align: right;">0.06 %</td>
</tr>
<tr>
<td>6</td>
<td style="text-align: right;"><tt>29 times</tt></td>
<td style="text-align: right;">0.05 %</td>
</tr>
<tr>
<td>8</td>
<td style="text-align: right;"><tt>18 times</tt></td>
<td style="text-align: right;">0.03 %</td>
</tr>
<tr>
<td>@</td>
<td style="text-align: right;"><tt>17 times</tt></td>
<td style="text-align: right;">0.03 %</td>
</tr>
<tr>
<td></td>
<td style="text-align: right;"><tt>14 times</tt></td>
<td style="text-align: right;">0.03 %</td>
</tr>
<tr>
<td>z</td>
<td style="text-align: right;"><tt>13 times</tt></td>
<td style="text-align: right;">0.02 %</td>
</tr>
<tr>
<td>5</td>
<td style="text-align: right;"><tt>13 times</tt></td>
<td style="text-align: right;">0.02 %</td>
</tr>
<tr>
<td>4</td>
<td style="text-align: right;"><tt>8 times</tt></td>
<td style="text-align: right;">0.01 %</td>
</tr>
<tr>
<td>?</td>
<td style="text-align: right;"><tt>8 times</tt></td>
<td style="text-align: right;">0.01 %</td>
</tr>
<tr>
<td>9</td>
<td style="text-align: right;"><tt>7 times</tt></td>
<td style="text-align: right;">0.01 %</td>
</tr>
</tbody>
</table>
<hr />
<h2 style="font-size: 90%;"><a href="#results">:: UP ::</a>Frequent pairs of
keys in your text</h2>
<table>
<tbody>
<tr>
<td>_Space__Space_</td>
<td style="text-align: right;"><tt>9243 times</tt></td>
<td style="text-align: right;">17.04 %</td>
</tr>
<tr>
<td>_NewLine__Space_</td>
<td style="text-align: right;"><tt>1233 times</tt></td>
<td style="text-align: right;">2.27 %</td>
</tr>
<tr>
<td>_Space__LeftShift_</td>
<td style="text-align: right;"><tt>805 times</tt></td>
<td style="text-align: right;">1.48 %</td>
</tr>
<tr>
<td>_LeftShift_(</td>
<td style="text-align: right;"><tt>674 times</tt></td>
<td style="text-align: right;">1.24 %</td>
</tr>
<tr>
<td>_LeftShift_)</td>
<td style="text-align: right;"><tt>673 times</tt></td>
<td style="text-align: right;">1.24 %</td>
</tr>
<tr>
<td>_LeftShift_&#8221;</td>
<td style="text-align: right;"><tt>563 times</tt></td>
<td style="text-align: right;">1.04 %</td>
</tr>
<tr>
<td>_LeftShift__</td>
<td style="text-align: right;"><tt>554 times</tt></td>
<td style="text-align: right;">1.02 %</td>
</tr>
<tr>
<td>se</td>
<td style="text-align: right;"><tt>549 times</tt></td>
<td style="text-align: right;">1.01 %</td>
</tr>
<tr>
<td>,_Space_</td>
<td style="text-align: right;"><tt>543 times</tt></td>
<td style="text-align: right;">1.00 %</td>
</tr>
<tr>
<td>_LeftShift_:</td>
<td style="text-align: right;"><tt>490 times</tt></td>
<td style="text-align: right;">0.90 %</td>
</tr>
<tr>
<td>el</td>
<td style="text-align: right;"><tt>405 times</tt></td>
<td style="text-align: right;">0.75 %</td>
</tr>
<tr>
<td>er</td>
<td style="text-align: right;"><tt>377 times</tt></td>
<td style="text-align: right;">0.70 %</td>
</tr>
<tr>
<td>in</td>
<td style="text-align: right;"><tt>364 times</tt></td>
<td style="text-align: right;">0.67 %</td>
</tr>
<tr>
<td>_Space__RightShift_</td>
<td style="text-align: right;"><tt>362 times</tt></td>
<td style="text-align: right;">0.67 %</td>
</tr>
<tr>
<td>or</td>
<td style="text-align: right;"><tt>352 times</tt></td>
<td style="text-align: right;">0.65 %</td>
</tr>
<tr>
<td>_LeftShift_&gt;</td>
<td style="text-align: right;"><tt>348 times</tt></td>
<td style="text-align: right;">0.64 %</td>
</tr>
<tr>
<td>_Space_i</td>
<td style="text-align: right;"><tt>344 times</tt></td>
<td style="text-align: right;">0.63 %</td>
</tr>
<tr>
<td>_Space_s</td>
<td style="text-align: right;"><tt>341 times</tt></td>
<td style="text-align: right;">0.63 %</td>
</tr>
<tr>
<td>te</td>
<td style="text-align: right;"><tt>340 times</tt></td>
<td style="text-align: right;">0.63 %</td>
</tr>
<tr>
<td>e_LeftShift_</td>
<td style="text-align: right;"><tt>338 times</tt></td>
<td style="text-align: right;">0.62 %</td>
</tr>
<tr>
<td>=_Space_</td>
<td style="text-align: right;"><tt>332 times</tt></td>
<td style="text-align: right;">0.61 %</td>
</tr>
<tr>
<td>_Space_=</td>
<td style="text-align: right;"><tt>321 times</tt></td>
<td style="text-align: right;">0.59 %</td>
</tr>
<tr>
<td>re</td>
<td style="text-align: right;"><tt>306 times</tt></td>
<td style="text-align: right;">0.56 %</td>
</tr>
<tr>
<td>lf</td>
<td style="text-align: right;"><tt>294 times</tt></td>
<td style="text-align: right;">0.54 %</td>
</tr>
<tr>
<td>)_NewLine_</td>
<td style="text-align: right;"><tt>281 times</tt></td>
<td style="text-align: right;">0.52 %</td>
</tr>
<tr>
<td>e_Space_</td>
<td style="text-align: right;"><tt>281 times</tt></td>
<td style="text-align: right;">0.52 %</td>
</tr>
</tbody>
</table>
</div>

Actually, I was disappointed: there seem to be no clear advantage of Dvorak or
Colemak, wrt QWERTY and, given the popularity of the latter, switching does not
seem to be a good idea...

   [1]: http://en.wikipedia.org/wiki/QWERTY
   [2]: http://en.wikipedia.org/wiki/Dvorak_Simplified_Keyboard
   [3]: http://en.wikipedia.org/wiki/Colemak
   [4]: http://www.codeaxe.co.uk/dvorak/
   [5]: http://webpy.org/
