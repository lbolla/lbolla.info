<?php
/*
Template Name: Me
*/
?>

<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title>Lorenzo Bolla's Home Page</title>
		<style type="text/css">
body{margin:0;padding:0;color:#555;font-family:lucida console,monaco,monospace}.page-wrap{width:35em;margin:1em auto;padding:5px 25px 30px 25px;background:white;border-radius:5px;-moz-border-radius:5px;-webkit-border-radius:5px}p,ul{font-size:1.2em;line-height:1.4em}a{color:#386794;text-decoration:none;}a:hover{color:#1d4c77;text-decoration:underline}a:visited,a:active{color:#6c88a2}li + li{margin-top:0.5em}p.caption{margin:0;padding:0;font-style:italic;color:#777;font-size:0.9em}div.figure{float:right;margin-top:20px}hr{color:#eee;border:1px solid #eee;background:#eee}blockquote{margin:0em 1em;padding:0.1em 1em;background:#eee}pre{margin:0em 1em;padding:1em 1em;background:#f7f7f7;overflow:auto}.body{clear:both;padding-top:5px}.clear{clear:both}code{color:#555}blockquote + center{margin-top:1em}.footnoteRef:target{background:#333;color:white;border-radius:0.2em}.footnotes li{border-top:1px solid #fff;border-bottom:1px solid #fff}.footnotes li:target{background:#F4F4F4;border-top:1px solid #CCC;border-bottom:1px solid #CCC}.footnotes li p{margin:0}.footnotes li * + *{margin-top:0.5em !important}
		</style>
		<script type="text/javascript">

		  var _gaq = _gaq || [];
		  _gaq.push(['_setAccount', 'UA-15875446-1']);
		  _gaq.push(['_trackPageview']);

		  (function() {
		    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
		    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
		    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
		  })();

		</script>
	</head>
	<body>
		<div class="page-wrap">
		<h1>Lorenzo Bolla's Home Page</h1>
		<div id="posts">
			<h2>Recent Blog Posts</h2>
			<ul>
			<?php query_posts('showposts=3'); while ( have_posts() ) : the_post() ?>
				<li><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></li>
			<?php endwhile; ?>
			</ul>
			<a href="<?php bloginfo('url'); ?>" title="<?php bloginfo('name'); ?>">All posts</a>
		</div>
		<div id="tags">
			<h2>Tags</h2>
			<?php wp_tag_cloud(''); ?>
		</div>
		<div id="web-accounts">
			<h2>Web Accounts</h2>
			<ul>
				<li><a href="https://github.com/lbolla/">Github</a></li>
				<li><a href="http://stackoverflow.com/users/1063605/lbolla">StackOverflow</a></li>
				<li><a href="http://www.linkedin.com/in/lorenzobolla">LinkedIn</a></li>
				<li><a href="/cv">CV</a></li>
			</ul>
		</div>
		<div id="contact">
			<h2>Contact</h2>
			<ul>
				<li>Email: lbolla@gmail.com</li>
				<li><a href="/keys/lbolla_gmail_com.asc">PGP Key</a></li>
			</ul>
		</div>
		</div>
	</body>
</html>
