#!/usr/bin/python

import web
import config
from view import render

urls = (
	'/(.*)', 'index',
)

class index:
	def GET(self, *args, **kwargs):
		return render.base(render.main(), 'Main')

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.internalerror = web.debugerror
	app.run()
