#!/usr/bin/env python

import os
import sys
from lxml import etree as ET

print sys.argv

infile   = sys.argv[1]
htmlfile = infile.split('.')[0] + '.out.html'
textfile = infile.split('.')[0] + '.out.txt'
tmpfile  = '/tmp/tmp.html'

doctype = '<!DOCTYPE HTML>'
content_type = ET.Element('meta')
content_type.set('http-equiv', 'Content-Type')
content_type.set('content', 'text/html;charset=utf-8')

doc = ET.HTML(open(infile, 'r').read())

# FIXME: remove all the awful inline CSS
doc.find('head').append(content_type)
html = doctype + ET.tostring(doc, method='html', encoding='utf8')

text = ET.tostring(doc, method='text', encoding='utf8')
open(textfile, 'w').write(text)

open(tmpfile, 'w').write(html)
os.system('tidy -i -clean -utf8 -ashtml -w 0 -o %s %s' % (htmlfile, tmpfile))
