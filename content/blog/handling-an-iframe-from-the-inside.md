---
categories:
  - "programming"
date: "2011-03-30"
tags:
  - "javascript"
title: "Handling an iframe from the inside"
---

If you've ever worked with `iframes` you've certainly run into the [same origin
policy][1].

From [here][2]:

> The same origin policy basically limits how scripts and frames on different
> domains can talk to each other. 

This is particularly bad if you want to resize an `iframe` to accomodate its
content, as this is not doable with simple CSS (to the best of my knowledge!).
It can be done using [`window.postMessage`][3], though.

[See a demo here][4].

Basically, the content of the `iframe` fires `postMessage`s to its parent window
and the window itself, i.e. the `iframe` container, handles them. Cool...

   [1]: http://en.wikipedia.org/wiki/Same_origin_policy
   [2]: http://www.onlineaspect.com/2010/01/15/backwards-compatible-postmessage/
   [3]: https://developer.mozilla.org/en/DOM/window.postMessage
   [4]: /junk/iframe/
