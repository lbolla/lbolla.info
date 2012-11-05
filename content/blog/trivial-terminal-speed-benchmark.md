# Trivial terminal speed benchmark

- author: lbolla
- category: programming
- tags: benchmark, linux
- summary: 
- date: 2010-04-28 16:59:01

----------------

Today, while playing with [st][1], I tried a very simple benchmark. Here it is:
    
    	$> time seq -f 'teeeeeeeeeeeeeeeeeeeeeeeeeeeeeest %g' 999999

Here are the results:
    
    	xterm: 0m28.508s
    	rxvt: 0m8.568s
    	st: 0m12.082s

All the terminals shared the same fonts, but [xterm][2] and [rxvt][3] had
`saveLines=1024` set for scrolling purposes, feature that [st][1] lacks.

Being [st][1] at such an early stage of development, I think this is a good
result.

   [1]: http://st.suckless.org
   [2]: http://invisible-island.net/xterm/
   [3]: http://sourceforge.net/projects/rxvt/
