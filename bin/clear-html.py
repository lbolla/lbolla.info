#!/usr/bin/env python

import os
import sys
import re

from lxml import etree as ET


CLEAN_HTML_RE = [
		(re.compile('&nbsp;'), ''),
		]

CLEAN_TEXT_RE = [
		(re.compile('\t+'), ''),
		(re.compile(' +'), ' '),
		(re.compile('\r'), ''),
		(re.compile('\n ?(\n *)+'), '\n\n'),
		(re.compile('\n$'), ''),
		]


def clean_text(text):
	for r, s in CLEAN_TEXT_RE:
		text = r.sub(s, text)
	return text


def clean_html(text):
	for r, s in CLEAN_HTML_RE:
		text = r.sub(s, text)
	return text


def clean_doc(doc):

	for item in doc.findall('.//meta') + \
			    doc.findall('.//style') + \
				doc.findall('.//content'):
		item.getparent().remove(item)

	head = doc.find('head')
	if head is not None:
		content_type = ET.Element('meta')
		content_type.set('http-equiv', 'Content-Type')
		content_type.set('content', 'text/html;charset=utf-8')
		head.append(content_type)

	diego = ET.Element('span')
	diego.text = 'Diego Fusaro'
	for i in [img for img in doc.findall('.//img') if img.get('src') == 'DiegoLogoAnim2.gif']:
		i.getparent().replace(i, diego)

	return doc


infile   = sys.argv[1]
htmlfile = infile.split('.')[0] + '.out.html'
textfile = infile.split('.')[0] + '.out.txt'
errfile  = infile.split('.')[0] + '.out.err'
tmpfile  = '/tmp/tmp.html'

doc = clean_doc(ET.HTML(clean_html(open(infile, 'r').read())))
doctype = '<!DOCTYPE HTML>'
html = doctype + ET.tostring(doc, method='html', encoding='utf8')
open(tmpfile, 'w').write(html)
os.system('tidy -i -clean -utf8 -ashtml -f %s -w 0 -o %s %s' % (errfile, htmlfile, tmpfile))

text = clean_text(ET.tostring(doc, method='text', encoding='utf8'))
open(textfile, 'w').write(text)
