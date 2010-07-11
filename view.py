from random import randint, sample
import web
import config

t_globals = dict(
	datestr=web.datestr,
	title="Lorenzo Bolla",
)

render = web.template.render('tmpl/', cache=config.cache, globals=t_globals)

render._keywords['globals']['render'] = render

nquotes = 10
top_min = 0
top_max = 600
left_min = 0
left_max = 800
width_min = 200
width_max = 500

def get_quotes_raw():
	quotes = [q.split('\n') for q in open('quotes.txt', 'r').read().split('\n\n')]
	return sample(quotes, min(len(quotes), nquotes))

def get_quotes():
	quotes = []
	for quote in get_quotes_raw():
		quotes.append({
			'lines': quote,
			'top':   '%spx' % randint(top_min, top_max),
			'left':  '%spx' % randint(left_min, left_max),
			'width': '%spx' % randint(width_min, width_max),
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
		page=render.admin(),
		)
