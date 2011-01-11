from random import randint, sample, choice
import web
import config

t_globals = dict(
	datestr=web.datestr,
	title="Lorenzo Bolla",
)

render = web.template.render('tmpl/', cache=config.cache, globals=t_globals)

render._keywords['globals']['render'] = render

def get_quotes_raw():
	quotes = [q.split('\r\n') for q in open(config.quotes['filename'], 'r').read().split('\r\n'*2)]
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
	return render.base(
		page=render.main(get_quotes()),
		)

def login():
	return render.base(
		page=render.login(),
		)

def admin():
	return render.base(
		page=render.admin(open(config.quotes['filename'], 'r').read()),
		)
