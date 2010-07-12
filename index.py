#!/usr/bin/python

import web
import config
import view
from view import render

urls = (
	'/admin/?(.*)', 'admin',
	'/login', 'login',
	'/logout', 'logout',
	'/(.+)', 'redirect',
	'/', 'index',
)

web.config.debug = False
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'))
app.internalerror = web.debugerror

class index:
	def GET(self, *args, **kwargs):
		return view.main()

class redirect:
	def GET(self, *args):
		raise web.seeother('/')

class login:
	def GET(self):
		return view.login()
	def POST(self):
		i = web.input()
		if i.username == 'lbolla' and i.password == 'test':
			session.logged_in = True
			raise web.seeother('/admin')
		else:
			session.logged_in = False
			raise web.seeother('/login')

class logout:
	def GET(self):
		session.logged_in = False
		raise web.seeother('/')

class admin:
	def GET(self, *args):
		if session.get('logged_in', False):
			return view.admin()
		else:
			raise web.seeother('/login')

if __name__ == '__main__':
	app.run()
