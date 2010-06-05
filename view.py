import web
import config

t_globals = dict(
	datestr=web.datestr,
	maintitle="Lorenzo's Homepage",
)

render = web.template.render('tmpl/', cache=config.cache, globals=t_globals)

render._keywords['globals']['render'] = render

