import os
import web

t_globals = dict(
	title="CSSearch",
)

tmpldir = os.path.join(os.path.dirname(__file__), 'tmpl/cssearch/')
render = web.template.render(tmpldir, cache=False, globals=t_globals)
render._keywords['globals']['render'] = render

class index:
    def GET(self, what):
        if what == 'js':
            return render.js()
        else:
            raise web.seeother('/')
