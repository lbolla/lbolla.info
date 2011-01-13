#!/usr/bin/env python

import os
import sys
import re
import logging

from lxml import etree as ET


CLEAN_HTML_RE = [
		(re.compile('\r'), ''),
		(re.compile('\n'), ''),
		(re.compile('&nbsp;'), ''),
		(re.compile('<content[^>]*>'), ''),
		(re.compile('<font[^>]*>'), ''),
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

	# FIXME: for each TD
	#        if it has a and br children
	#        then probably is a ul
	#        substitute
	#
	# list_re = re.compile('<td>(.+)</td>')
	# list = list_re.search(text)
	# if list is not None:
	#     ul = ET.Element('ul')
	#     for item in list.groups()[0].split('<br>'):
	#         li = ET.Element('li')
	#         li.text = item
	#         ul.append(li)
	#     start, end = list.span()
	#     text[start:end] = ET.tostring(ul)

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


def flatten(a):
	if a.text:
		text = a.text.strip()
	else:
		text = ''.join(map(lambda x: x.text, a.getchildren())).strip()
	return text


def clean_for_md(doc):

	for a in doc.findall('.//strong'):
		if len(list(a.iterancestors('a'))) == 0:
			new_a = ET.Element('span')
			new_a.text = '*%s*' % flatten(a)
			a.getparent().replace(a, new_a)

	for a in doc.findall('.//a'):
		if a.get('href'):
			new_a = ET.Element('span')
			new_a.text = '[%s](%s)' % (flatten(a) , a.get('href'))
			a.getparent().replace(a, new_a)
		else:
			a.getparent().remove(a)
	
	return doc


logging.basicConfig(level=logging.DEBUG)

infile = sys.argv[1]
if len(sys.argv) > 1:
	outdir = sys.argv[2]
else:
	outdir = '/tmp'

inbase = os.path.basename(infile)
inbase = os.path.splitext(inbase)[0]

htmlfile = os.path.join(outdir, inbase + '.html')
textfile = os.path.join(outdir, inbase + '.txt')
errfile  = os.path.join(outdir, inbase + '.err')
tmpfile  = '/tmp/tmp.html'

doc = clean_doc(ET.HTML(clean_html(open(infile, 'r').read())))
doctype = '<!DOCTYPE HTML>'
html = doctype + ET.tostring(doc, method='html', encoding='utf8')
open(tmpfile, 'w').write(html)
os.system('tidy -i -clean -utf8 -ashtml -f %s -w 0 -o %s %s' % (errfile, htmlfile, tmpfile))

text = clean_text(ET.tostring(clean_for_md(doc), method='text', encoding='utf8'))
open(textfile, 'w').write(text)
