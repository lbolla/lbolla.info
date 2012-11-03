# py2dot

- title: py2dot
- author: lbolla
- category: programming
- tags: programming python graph graphviz
- summary: 
- post_id: 81
- date: 2008-10-05 14:17:12
- post_date_gmt: 2008-10-05 12:17:12
- comment_status: open
- post_name: py2dot
- status: publish
- post_type: post

----------------

[caption id="attachment_73" align="alignnone" width="572" caption="py2dot example"]![py2dot example][1][/caption] py2dot is a python script to generate graphs from a  python program. it interprets a python program as a graphs of function calls. it can represent classes and imported modules. [py2dot is available from pypi][2]. more information are available [here][3].

   [1]: http://lbolla.info/blog/wp-content/uploads/2008/10/complicated.png (py2dot)
   [2]: http://pypi.python.org/pypi/py2dot/ (pypi)
   [3]: http://lbolla.wordpress.com/py2dot/ (py2dot)

## Comments

**[mud_saisem](#53 "2010-12-14 06:38:58"):** it would help if it explains what the following means NameError: global name 'EXCLUDE_CLASSES' is not defined The example on the website does not even work. And there are just about no comments explaining in detail what each class does.

**[lbolla](#54 "2010-12-14 11:48:40"):** the code runs fine in Python 2.5, 2.6 and 2.7. I haven't tried Python 3.x. what version of Python are you using? the classes are pretty straightforward and mostly wrappers to easily handler syntax tokens from the Python parser. I suggest you to have a look at the parser standard module.

**[mud_saisem](#55 "2010-12-14 22:56:27"):** Do you have documentation on py2dot ? Using the help(py2dot) tells you about all the classes and methods but there are not comments of documented information explaining what each thing does. How do I know what each class does ? I have managed to get your example to work, and ran it over a script that uses multiple modules that it imports and it contains multiple classes itself. The output of py2dot is simply the name of the script.

