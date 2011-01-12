#!/usr/bin/env python

import os
import sys
from lxml import etree as ET

print sys.argv

infile = sys.argv[1]
outfile = sys.argv[2]
tmpfile = '/tmp/tmp.html'

doctype = '<!DOCTYPE HTML>'
content_type = ET.Element('meta')
content_type.set('http-equiv', 'Content-Type')
content_type.set('content', 'text/html;charset=utf-8')

doc = ET.HTML(open(infile, 'r').read())
doc.find('head').append(content_type)
# FIXME: remove all the awful inline CSS

html = doctype + ET.tostring(doc, method='html')

open(tmpfile, 'w').write(html)
os.system('tidy -i -clean -ashtml -w 0 -o %s %s' % (outfile, tmpfile))
