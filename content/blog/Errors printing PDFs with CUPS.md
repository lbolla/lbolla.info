---
title: Errors printing PDFs with CUPS
date: 2012-09-13
tags:
- linux
---
This is another of those posts *to not forget*. If printing a PDF file with `lp` prints a blank page with error messages like:

```
ERROR: configurationerror OFFENDING COMMAND: setpagedevice STACK: --nostringval-- ...
```

the problem is probably that your PDF has a certain page size (let\'s say *letter*) but your printer expects another (let\'s say *A4*).

Check your printer settings and your PDf (with `lpinfo pdffile`) to verify. If this is the case, print with this command instead:

```shell
lp -o fit-to-page pdffile
```
