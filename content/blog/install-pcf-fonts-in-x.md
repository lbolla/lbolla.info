# installing pcf fonts in X

- title: installing pcf fonts in X
- author: lbolla
- category: programming
- tags: font,linux
- summary: 
- post_id: 138
- date: 2010-01-07 18:55:00
- post_date_gmt: 2010-01-07 16:55:00
- comment_status: open
- post_name: install-pcf-fonts-in-x
- status: publish
- post_type: post

----------------

as I keep forgetting, here is how to install pcf fonts in X 

  1. create a new directory for the fonts, usually under /usr/share/fonts: `$> mkdir /usr/share/fonts/`
  2. copy the pcf file(s) into it (sometimes the pcf files are gzipped): `$> cp /path/to/pcf/*.pcf* /usr/share/fonts/`
  3. run mkfontdir, to create a fonts.dir file, used by X to find font files `$> mkfontdir /usr/share/fonts/`
  4. add the new dir to X font path. The easiest way to do it is to stick this line in your .xinitrc: `xset fp+ /usr/share/fonts/`
now your new font should compare in xfontsel and you should be able to use it as normal. by the way, [this][1] is a very nice font for programming!

   [1]: http://www.proggyfonts.com/

## Comments

**[Download Fonts](#862 "2012-02-28 05:42:20"):** thankyou for the easy guide, I too keep forgetting how to install these fonts. keep it up

