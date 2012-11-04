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

## Comments

**[Venus098](#56 "2009-04-12 02:20:49"):** can I ask why is having validated code so important? I can see why having an accessible site is important, but I fail to see how the two are connected.

**[lbolla](#57 "2009-04-12 11:48:20"):** for a long answer, I recommend [this link][4]. my own personal (short) answer is that a "valid" html is safer, more portable and more "honest" to the final user. safer because sticking to the rules avoids trivial programming errors. more portable because all standard compliant browsers (not many today, but the number is increasing every day...) will render standard pages in the same way and testing will be easier. more honest because using browser-dependent "features" (here including the exploitation of browser-dependent "bugs") is going to break the site as soon as the user tries to use another browser: the consequence is that the average user will revert to the previous, buggy one in order to view the non-standard compliant website, keeping it alive... and we all want non-standard compliant browsers to die, don't we? standards are there so that people do not need to reinvent the wheel or support someone else's wheels, too...

