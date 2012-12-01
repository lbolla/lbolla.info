# Installing pcf fonts in X

- author: lbolla
- category: programming
- tags: linux, X
- summary: 
- date: 2010-01-07 18:55:00

----------------

As I keep forgetting, here is how to install `pcf` fonts in X 

  1. Create a new directory for the fonts, usually under /usr/share/fonts:

        $> mkdir /usr/share/fonts/

  2. Copy the `pcf` file(s) into it (sometimes the `pcf` files are gzipped):

        $> cp /path/to/`pcf`/*.`pcf`* /usr/share/fonts/

  3. Run mkfontdir, to create a fonts.dir file, used by X to find font files

        $> mkfontdir /usr/share/fonts/

  4. Add the new dir to X font path. The easiest way to do it is to stick this
     line in your `.xinitrc`:

        xset fp+ /usr/share/fonts/

Now your new font should compare in `xfontsel` and you should be able to use it as normal.

By the way, [this][1] is a very nice font for programming!

   [1]: http://www.proggyfonts.com/
