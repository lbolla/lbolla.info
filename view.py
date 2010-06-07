import datetime
import logging
import web
import wordpresslib
import lastfm
import config
import formatting

t_globals = dict(
	fmt=formatting,
	maintitle="Lorenzo's Homepage",
)

render = web.template.render('tmpl/', cache=config.cache, globals=t_globals)

render._keywords['globals']['render'] = render

def get_wp_posts():
	try:
		url = 'http://lbolla.wordpress.com/xmlrpc.php'
		c = wordpresslib.WordPressClient(url, config.wp_login, config.wp_passwd)
		c.selectBlog(0)
		return sorted(c.getRecentPosts(3), key=lambda x: x.date, reverse=True)
	except Exception, e:
		logging.error('Error fetching wp posts: %s' % e)
		return None

def get_lastfm_tracks():
	try:
		api = lastfm.Api(config.lastfm_api_key)
		user = api.getUser(config.lastfm_user)
		# return sorted(user.lovedTracks, key=lambda x: x.lovedOn or datetime.datetime(1970,1,1), reverse=True)[:10]
		return sorted(user.recentTracks, key=lambda x: x.playedOn or datetime.datetime(1970,1,1), reverse=True)[:10]
	except Exception, e:
		logging.error('Error fetching lastfm songs: %s' % e)
		return None

def main():
	return render.base(
		page=render.main(
			wp_posts=get_wp_posts(),
			lastfm_tracks=get_lastfm_tracks(),
			),
		title='Main')
