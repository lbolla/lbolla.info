#!/usr/bin/python

import web

render = web.template.render('tmpl')

urls = (
	'/(.*)', 'Main',
)

class Main:
	def GET(self, *args, **kwargs):
		return render.index()

web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
