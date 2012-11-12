# Useful scripts - csvfmt, xmlfmt, jsonfmt

- title: Useful scripts - csvfmt, xmlfmt, jsonfmt
- author: lbolla
- category: programming
- tags: useful-scripts, python
- summary: Useful scripts to format CSV, XML and JSON files for easier reading
- date: 2012-11-12 13:14:52

----------------

This is the third post of a [series][1] describing simple scripts that
I wrote to ease my life as a programmer.

In this post, I'll describe 3 scripts to "pretty print" some common
file types, to improve readability: [`csvfmt`][2], [`xmlfmt`][3] and
[`jsonfmt`][4].

[`csvfmt`][2] takes a `CSV` ("Comma Separated Values") file from
`stdin`, parses it and pretty print each record as a Python
dictionary.

    #!/usr/bin/env python
    
    import csv
    import sys
    import pprint
    
    for row in csv.DictReader(sys.stdin):
        pprint.pprint(row)

Output looks like this:

    % echo 'a,b,c
    1,2,3
    4,5,6
    ' | csvfmt
    {'a': '1', 'b': '2', 'c': '3'}
    {'a': '4', 'b': '5', 'c': '6'}

[`xmlfmt`][3] takes an `XML` file from either `stdin` or a file
(specified on the cmd line) and extracts all the text from it. This
script is thought to be used to read the text embedded in `XML` tags,
and it's analogous to `[htmlfmt`][5]. If you want to format an `XML`
file, maintaining the `XML` tags, use `[xmllint -format`][6], or my
`[xmlind`][7] (described another blog post of this series.)

    #!/usr/bin/env python
    
    import xml.dom.minidom
    from pylib.xmlutil import getText, getInput
    
    dom = xml.dom.minidom.parse(getInput())
    print(getText(dom))

For example:

    % echo '<a>a text<b>b text</b>more a text</a>' | xmlfmt
    a textb textmore a text

[`jsonfmt`][4] takes a `JSON` file from `stdin` and pretty prints it as
a Python object.

    #!/usr/bin/env python
    
    import json
    import sys
    import pprint
    
    pprint.pprint(json.load(sys.stdin))

Try it out:

    $> curl 'http://search.twitter.com/search.json?q=lorenzo' | jsonfmt
    {u'completed_in': 0.035,
     u'max_id': 267982040698351617L,
     u'max_id_str': u'267982040698351617',
     u'next_page': u'?page=2&max_id=267982040698351617&q=lorenzo',
     u'page': 1,
     u'query': u'lorenzo',
     u'refresh_url': u'?since_id=267982040698351617&q=lorenzo',
     u'results': [{u'created_at': u'Mon, 12 Nov 2012 13:27:52 +0000',
                   u'from_user': u'michael_174',
                   u'from_user_id': 234373960,
                   u'from_user_id_str': u'234373960',
                   u'from_user_name': u'Michael Adhiyatama',
                   u'geo': None,
                   u'id': 267982040698351617L,
                   u'id_str': u'267982040698351617',
                   u'iso_language_code': u'in',
     etc. etc.

All three scripts are written in Python and available [here][8].

   [1]: /blog/tag/#useful-scripts
   [2]: https://github.com/lbolla/cmd/blob/master/csvfmt
   [3]: https://github.com/lbolla/cmd/blob/master/xmlfmt
   [4]: https://github.com/lbolla/cmd/blob/master/jsonfmt
   [5]: http://man.cat-v.org/plan_9/1/fmt
   [6]: http://xmlsoft.org/xmllint.html
   [7]: https://github.com/lbolla/cmd/blob/master/xmlind
   [8]: https://github.com/lbolla/cmd
