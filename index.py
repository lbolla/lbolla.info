#!/usr/bin/python

import web
import config
import view
from view import render

urls = (
	'/(.*)', 'index',
)

class index:
	def GET(self, *args, **kwargs):
		return view.main()

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.internalerror = web.debugerror
	app.run()
