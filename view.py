from random import randint, sample
import web
import config

t_globals = dict(
	datestr=web.datestr,
	title="Lorenzo Bolla",
)

render = web.template.render('tmpl/', cache=config.cache, globals=t_globals)

render._keywords['globals']['render'] = render

def get_quotes_raw():
	quotes = [q.split('\r\n') for q in open(config.quotesfile, 'r').read().split('\r\n'*2)]
	return sample(quotes, min(len(quotes), config.nquotes))

def get_quotes():
	quotes = []
	for quote in get_quotes_raw():
		quotes.append({
			'lines': quote,
			'top':   '%d%%' % randint(0, 100),
			'left':  '%d%%' % randint(0, 100),
			'width': '%sem' % randint(config.width_min, config.width_max),
			})
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
		page=render.admin(open(config.quotesfile, 'r').read()),
		)
