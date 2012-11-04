# CVS behind a firewall through an http proxy

- author: lbolla
- category: links,programming
- tags: cvs, firewall, proxy
- summary: How to avoid firewalls
- date: 2008-04-21 13:45:37

----------------

If you work in a company with a too restrictive firewall, but you still need to
access a CVS repository like [Sourceforge][1], you can bypass it using the
program [connect.c][2].

From [here][2]: 

> connect.c is the simple relaying command to make network connection via SOCKS
> and https proxy. It is mainly intended to be used as proxy command of
> OpenSSH.

Just download it and compile it (for windows users there is a precompiled
`connect.exe`). Then, if you want to use the SOCKS server `socks.local.net` to
access the internet, add these two lines to your `.ssh/config`:
    
    Host remote.outside.net
    ProxyCommand connect -S socks.local.net %h %p

In my case, I use an http proxy to access the internet, instead of the SOCSK,
and I do not want to use `connect.exe` for internal repositories. Hence, my
`.ssh/config` contains: 
    
    Host empy.cvs.sourceforge.net
    ProxyCommand connect -H proxy.company.net:80 %h %p

Enjoy!

   [1]: http://www.sourceforge.net (sorceforge)
   [2]: http://www.meadowy.org/~gotoh/projects/connect (connect)