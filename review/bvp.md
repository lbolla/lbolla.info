# bvp

- title: bvp
- author: lbolla
- category: programming
- tags: bvp,programming,python
- summary: 
- post_id: 63
- date: 2008-04-14 20:04:20
- post_date_gmt: 2008-04-14 18:04:20
- comment_status: open
- post_name: bvp
- status: publish
- post_type: post

----------------

for you, Python lover, who always needs Matlab functions: boundary value problems are not a problem anymore. Googling for a [bvp4c][1] clone, I ended up [here][2]: 

> This is a Python wrapper for a [modified][3] version of the [COLNEW][4] boundary value problem solver by U. Ascher and G. Bader. Modifications made include vectorization over mesh points and better compatibility with Python.

there are little differences in the usage, though. I tried to reproduce the examples in [this tutorial][5], to clarify things. You can download the first two examples [here][6]. enjoy!

   [1]: http://www.mathworks.com/access/helpdesk/help/techdoc/index.html?/access/helpdesk/help/techdoc/ref/bvp4c.html&http://www.google.com/cse?cx=002683415331144861350%3Atsq8didf9x0&q=bvp4c&ie=utf-8&oe=utf-8&cof=FORID%3A1&sa=Search (bvp4c)
   [2]: http://www.elisanet.fi/ptvirtan/software/bvp/index.html (BVP)
   [3]: http://www.elisanet.fi/ptvirtan/software/bvp/colnew.f.diff
   [4]: http://www.netlib.org/ode/colnew.f
   [5]: http://www.mathworks.com/matlabcentral/fileexchange/loadFile.do?ref=bvp_tutorial&objectId=3819&objectType=file (bvp_tutorial)
   [6]: http://www.box.net/shared/2akb4asoo0 (bvp_tutorial)

## Comments

**[jsalvati](#41 "2008-11-04 14:28:17"):** I too was very happy to find this. I am sorta surprised it has not been made into a SciPy component.

**[bastian weber](#42 "2009-01-31 12:02:01"):** Thanks for adapting the two first examples. They helped me significantly in understanding how to formulate the boundary conditions the right manner. As I needed solve a problem with unknown parameters I tackled example 3 which dedicates to that topic. http://paste.pocoo.org/show/102102/

**[Mauricio Angeles](#43 "2009-03-05 00:16:38"):** Hi, Thanks. It is great that such a numerical tool is around. I tried to install but there is a problem when I built it. The numerical libraries aren't in the path. I am running a Ubuntu Intrepid and I installed the a bundle (Enthought) that included numpy and scipy. Any idea?

**[lbolla](#44 "2009-03-05 01:48:44"):** Hi Mauricio. I installed sooo much time ago... by compiling everything from scratch. What libraries are you missing?

**[Miha](#45 "2010-03-12 16:23:59"):** Mauricio: I had problems with building (on debian squeeze) too. I got an error, which said that i don't have atlas in /usr/lib, even though i had a file libatlas.so.3gf. I tried to fix the problem by making a symbolic link libatlas.so, but that didn't help. To tell the long story short: i didn't have the right libatlas package installed. When i installed libatlas-base-dev, sudo apt-get install libatlas-base-dev everything started to work.

**[Mauricio](#46 "2010-04-30 02:06:35"):** Miha, Thanks, I needed it a long time ago for my PhD thesis and I had forgotten about it for a while since I couldn't install it. I finally picked it up and managed to install and test the scikit which worked perfectly. Thanks Lorenzo. I remember that I couldn't compile from source at that time. The scikit was definitely easier. I only installed setuptools and python-dev and run the easy_install command.

