---
title: Command line HTML validator
date: 2009-01-30
---
Valid HTML is something we should strive to achieve. [W3C Validator](http://validator.w3.org/) is an invaluable tool to do just that. Unfortunately, validating a local file you are working on can be annoying after the 100th time you\'ve uploaded it to the [W3C website](http://validator.w3.org/).

[Here](https://raw.github.com/lbolla/junk/master/utils/w3c_validate.py) you can find a [command line HTML validator](https://raw.github.com/lbolla/junk/master/utils/w3c_validate.py) that simply uploads anything passed to it from `stdin` to the [W3C Validator](http://validator.w3.org/). The basic syntax is:

``` shell
$> python validate.py < file_to_validate.html
```

It requires [html2text](http://www.aaronsw.com/2002/html2text/) to print the detailed list of errors.

Enjoy!
