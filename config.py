import os
import web

web.config.debug = False

# avoids showing index.py in url
# http://webpy.org/cookbook/cgi-apache
home = ''
os.environ["SCRIPT_NAME"] = home
os.environ["REAL_SCRIPT_NAME"] = home

hostname = os.uname()[1]
if hostname not in ('laptop', 'garfield', 'eee'):
	# runs as FastCGI
	web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)

# use cache for templates?
cache = False

admin_key = '42638a329474f850fca989f4e51a041b'

quotes = {
		'filename'  : 'quotes.txt',
		'n_min'     : 3,
		'n_max'     : 10,
		'width_min' : 20,
		'width_max' : 50,
		}

