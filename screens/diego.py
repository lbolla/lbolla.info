import web

t_globals = dict(
	datestr=web.datestr,
	title="Filosofico.net",
)
render = web.template.render('tmpl/diego/', cache=False, globals=t_globals)

render._keywords['globals']['render'] = render

class diego:
	def GET(self, *args, **kwargs):
		return render.base(
			page=render.main(),
			)
