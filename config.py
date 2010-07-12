import os
import web

hostname = os.uname()[1]
if hostname not in ('laptop', 'garfield'):
	# runs as FastCGI
	web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)

# use cache for templates?
cache = False
