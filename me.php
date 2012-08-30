<?php
/*
Template Name: Me
 */
?>

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Lorenzo Bolla</title>
        <link href="/static/css/me.css" media="all" rel="stylesheet" type="text/css">
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
        <div id="gravatar">
	<?php 
	   echo get_avatar( 'lbolla@gmail.com', $size = '50'); 
	   ?>
	</div>
        <div class="page-wrap">
        <h1>Lorenzo Bolla</h1>
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
