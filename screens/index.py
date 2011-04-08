#!/usr/bin/env python

try:
	from hashlib import md5
except ImportError:
	from md5 import md5

import web
import config
import view
from view import render
import diego

urls = (
	'/diego/authors/(.+)', 'diego.author',
	'/diego/?(.*)', 'diego.index',
	'/admin/?(.*)', 'admin',
	'/login', 'login',
	'/logout', 'logout',
	'/(.+)', 'redirect',
	'/', 'index',
)

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
		if md5(i.username + i.password).hexdigest() == config.admin_key:
			session.logged_in = True
			raise web.seeother('/admin')
		else:
			session.logged_in = False
			raise web.seeother('/login')

class logout:
	def GET(self):
		session.logged_in = False
		session.kill()
		raise web.seeother('/')

class admin:
	def GET(self, *args):
		if session.get('logged_in', False):
			return view.admin()
		else:
			raise web.seeother('/login')
	def POST(self, *args):
		i = web.input()
		open(config.quotes['filename'], 'w').write(i.quotes)
		raise web.seeother('/admin')

if __name__ == '__main__':
	app.run()
