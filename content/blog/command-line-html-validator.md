# Command line HTML validator

- author: lbolla
- category: programming
- tags: html, python
- summary: Command line HTML validator
- date: 2009-01-31 23:00:22

----------------

Valid HTML is something we should strive to achieve. [W3C Validator][1] is an
invaluable tool to do just that. Unfortunately, validating a local file you are
working on can be annoying after the 100th time you've uploaded it to the [W3C
website][1].

[Here][2] you can find a [command line HTML validator][2] that
simply uploads anything passed to it from `stdin` to the [W3C Validator][1]. The
basic syntax is:

    $> python validate.py < file_to_validate.html

It requires [html2text][3] to print the detailed list of errors.

Enjoy!

   [1]: http://validator.w3.org/ (W3C Validator)
   [2]: https://raw.github.com/lbolla/junk/master/utils/w3c_validate.py (html validator)
   [3]: http://www.aaronsw.com/2002/html2text/ (html2text)
   [4]: http://validator.w3.org/docs/why.html
