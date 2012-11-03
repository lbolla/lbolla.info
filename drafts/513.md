# Acme editor

- title: Acme editor
- author: lbolla
- category: programming
- tags: acme,tutorial
- summary: 
- post_id: 513
- date: 2012-11-01 14:20:56
- post_date_gmt: 
- comment_status: open
- post_name: 
- status: draft
- post_type: post

----------------

# Why?

Rob Pike uses it: http://rob.pike.usesthis.com/ 

# Setup

Get source with $> hg clone http://code.swtch.com/plan9port plan9port Compile with: $> ./INSTALL Run with: $> 9 acme 

## Plumbing

You need plumber(4) running in order to use plumb(1): $> 9 plumber Then you can mouse-3 click on pdfs, images, urls etc. and tie actions to those files. Predefined actions are in $PLAN9/plumb/initial.plumbing . To poke around, mount it and explore it: $> 9pfuse unix!/tmp/ns.$USER.:0/plumb /tmp/plumb Show my $HOME/lib/plumbing - antiword for docx, xlsx, etc. - xmlfmt, xmlind 

# Fonts

PELM for proper unicode (see screenshot PISPO Arabic). fixed for coding (screenshot). use fontsrv 

# Scripts

Indent: a+, a- Auto-indenting Commenting Watching adict (from rsc video) 

## Mail

http://9fans.net/archive/2009/12/213 

> 1) build and install mailfs cd $PLAN9/src/cmd/upas/ mk install cd nfs mk install 2) configuration cd $PLAN9/log; chmod 666 smtp smtp.debug smtp.fail mail >smtp 
>
>> smtp.debug >smtp.fail >mail cd $PLAN9/mail/lib edit rewrite optionnally edit remotemail 
> 
> 3) authentication factotum factotum -g 'proto=pass service=imap server=your.imap.server user=you_there !password?' 4) run it! mailfs -t your.imap.server (-t is for tls) button 2 exec on 'Mail' in acme (without the quotes) (you need the plumber running for everything to work as expected in acme) 

Example: 123-reg.co.uk mail $> factotum -g 'proto=pass service=imap server=imap.123-reg.co.uk user=lorenzo.bolla@pispo.co.uk !password?' $ ls /tmp/ns.lollo.:0/ acme factotum plumb $ 9 mailfs imap.123-reg.co.uk 

# Tools

Decent 3-button mouse 

# Hints for VI users

It needs time to get used to using a mouse! Take your time: use acme only few hours a day, maybe VI in the morning and acme in the afternoon, until you get used to it! 

# What I miss most

Autocompletion: I misstype a lot... 

# Resources

Russ Cox: http://research.swtch.com/acme TODO: 

  * Mail: http://9fans.net/archive/2009/12/213
  * Find a decent font (see PISPO arabic xlations) 
    * use fontsrv
  * Fuse mount 
    * /tmp/acme is mounted with "w" priviledges
    * can't write to ctl files (Slide script)
  * Rule to open dir in the same window 
    * show also ..