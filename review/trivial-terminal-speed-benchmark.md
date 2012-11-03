# trivial terminal speed benchmark

- title: trivial terminal speed benchmark
- author: lbolla
- category: programming
- tags: benchmark,rxvt,speed,st,xterm
- summary: 
- post_id: 161
- date: 2010-04-28 16:59:01
- post_date_gmt: 2010-04-28 14:59:01
- comment_status: open
- post_name: trivial-terminal-speed-benchmark
- status: publish
- post_type: post

----------------

today, while playing with [st][1], I tried a very simple benchmark. here it is:
    
    	$> time seq -f 'teeeeeeeeeeeeeeeeeeeeeeeeeeeeeest %g' 999999
    

here are the results:
    
    	xterm: 0m28.508s
    	rxvt: 0m8.568s
    	st: 0m12.082s
    

all the terminals shared the same fonts, but [xterm][2] and [rxvt][3] had `saveLines=1024` set for scrolling purposes, feature that [st][1] lacks.

being [st][1] at such an early stage of development, I think this is a good result.

   [1]: http://st.suckless.org
   [2]: http://invisible-island.net/xterm/
   [3]: http://sourceforge.net/projects/rxvt/