# escape sequences for rxvt

- title: escape sequences for rxvt
- author: lbolla
- category: programming
- tags: code,escape,rxvt,vim
- summary: 
- post_id: 117
- date: 2009-05-01 10:07:06
- post_date_gmt: 2009-05-01 08:07:06
- comment_status: open
- post_name: escape-sequences-for-rxvt
- status: publish
- post_type: post

----------------

I'm posting this info because I had a hard time searching for it on the internet. if you are using rxvt (or urxvt), and you want escape sequences to work as in xterm, you need to specify them in your .Xdefaults. here are the codes I had to add to have vim working properly on rxvt (I use alt-left_arrow and alt-right_arrow to navigate through tabs): *Rxvt*meta8: false *Rxvt.keysym.C-Left: +033[1;5D *Rxvt.keysym.C-Right: +033[1;5C *Rxvt.keysym.M-Left: +033[1;3D *Rxvt.keysym.M-Right: +033[1;3C (substitute "+" with "") enjoy!

## Comments

**[Ingo](#62 "2010-06-03 22:15:58"):** You made my day ! That's absolutely what I was looking for - to also get the shell working again correctly (ctrl-left|right for word jumps) in urxvt with tabbing enabled

**[Alexander](#63 "2010-09-29 21:02:55"):** God bless you! Thank you SO MUCH for that hack! P.S. I also add a combination for up and down arrows which looks like that *Rxvt.keysym.C-Up: +033[1;5A *Rxvt.keysym.C-Down: +033[1;5B (substitute “+” with “”)

