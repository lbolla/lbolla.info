import logging
import StringIO
import markdown
import web

class md_render(web.template.render):
	"""Markdown aware renderer."""
	def play(self, name):
		tmpl = self._template(name).filename
		if tmpl.endswith('.md'):
			output = StringIO.StringIO()
			markdown.markdownFromFile(input=tmpl, output=output, encoding='utf-8')
			return self.base(main=output.getvalue())
		else:
			return self.base(getattr(self, name)())

t_globals = dict(
	datestr=web.datestr,
	title="Filosofico.net",
)
render = md_render('tmpl/diego/', cache=False, globals=t_globals) # Note: don't use base kw here!
render._keywords['globals']['render'] = render

class index:
	def GET(self, *args):
		return render.play('main')

class author:
	def GET(self, name):
		try:
			return render.play(name)
		except Exception, e:
			logging.error('Error in author: %s', e)
			raise web.seeother('/diego')
