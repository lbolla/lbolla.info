import os
import web

hostname = os.uname()[1]
if hostname not in ('laptop', 'garfield', 'eee'):
	# runs as FastCGI
	web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)

# use cache for templates?
cache = False

quotesfile = 'quotes.txt'
nquotes = 10
width_min = 20
width_max = 50

