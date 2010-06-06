import logging
import web
import wordpresslib
import config
import secret

t_globals = dict(
	datestr=web.datestr,
	maintitle="Lorenzo's Homepage",
)

render = web.template.render('tmpl/', cache=config.cache, globals=t_globals)

render._keywords['globals']['render'] = render

def get_last_blog_post():
	try:
		url = 'http://lbolla.wordpress.com/xmlrpc.php'
		c = wordpresslib.WordPressClient(url, secret.bloglogin, secret.blogpasswd)
		c.selectBlog(0)
		return c.getLastPost()
	except Exception, e:
		logging.error('Error fetching last blog post: %s' % e)
		return None

def main():
	return render.base(
		page=render.main(
			last_blog_post=get_last_blog_post(),
			),
		title='Main')
