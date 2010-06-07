import os
import web
from secret import *

hostname = os.uname()[1]
if hostname not in ('laptop', 'garfield'):
	# runs as FastCGI
	web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)

# use cache for templates?
cache = False
