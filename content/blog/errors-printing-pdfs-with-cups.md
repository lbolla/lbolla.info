---
categories:
  - "programming"
date: "2012-09-13"
description: "None"
tags:
  - "cups"
title: "Errors printing PDFs with CUPS"
---

This is another of those posts _to not forget_. If printing a PDF file with
`lp` prints a blank page with error messages like: 

> ERROR: configurationerror OFFENDING COMMAND: setpagedevice STACK: --nostringval-- ...

the problem is probably that your PDF has a certain page size (let's say
_letter_) but your printer expects another (let's say _A4_).

Check your printer
settings and your PDf (with `lpinfo pdffile`) to verify. If this is the case,
print with this command instead:

    lp -o fit-to-page pdffile
