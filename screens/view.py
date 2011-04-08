from random import randint, sample, choice
import os
import web
import config

t_globals = dict(
	datestr=web.datestr,
	title="Lorenzo Bolla",
)

tmpldir = os.path.join(os.path.dirname(__file__), 'tmpl')
render = web.template.render(tmpldir, base='base', cache=config.cache, globals=t_globals)

render._keywords['globals']['render'] = render

def get_quotes_raw():
	try:
		quotes = [q.split('\r\n') for q in open(config.quotes['filename'], 'r').read().split('\r\n'*2)]
	except IOError:
		quotes = []
	return sample(quotes, min(len(quotes), randint(config.quotes['n_min'], config.quotes['n_max'])))

def get_quotes():
	quotes = []
	for quote in get_quotes_raw():
		css = 'position:absolute;width:%sem;%s:%d%%;%s:%d%%;' % \
				(randint(config.quotes['width_min'], config.quotes['width_max']),
						choice(('top', 'bottom')), randint(0, 30),
						choice(('left', 'right')), randint(0, 30))
		quotes.append({'lines': quote, 'css': css})
	return quotes

def main():
	return render.main(get_quotes())

def login():
	return render.login()

def admin():
	return render.admin(open(config.quotes['filename'], 'r').read())
