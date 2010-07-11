#!/usr/bin/python

import web
import config
import view
from view import render

urls = (
	# '/admin/?(.*)', 'admin',
	'/(.*)', 'index',
)

class index:
	def GET(self, *args, **kwargs):
		return view.main()

class admin:
	def GET(self, *args):
		return view.admin()

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.internalerror = web.debugerror
	app.run()
