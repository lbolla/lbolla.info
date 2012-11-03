# editors' speed on opening big files

- title: editors' speed on opening big files
- author: lbolla
- category: programming
- tags: big,ed,file,open,sam,vim
- summary: 
- post_id: 165
- date: 2010-05-17 15:05:47
- post_date_gmt: 2010-05-17 13:05:47
- comment_status: open
- post_name: editors-speed-on-opening-big-files
- status: publish
- post_type: post

----------------

while playing with different editors (namely [vim][1] and [sam][2]) I tried to time how long some common editors take to open a big file (~140Mb).

here are the results:

editor
real
user
sys

`ed`
4.866s
3.440s
3.440s

`vim`
2.086s
0.836s
0.232s

`nano`
16.264s
15.361s
0.172s

`sam`
way too long

then, for curiosity, I timed `less` with and without (`-n`) line numbering:

`less`
3.552s
0.200s
0.072s

`less -n`
0.182s
0.016s
0.016s

not sure what to do with these numbers, yet...

   [1]: http://www.vim.org
   [2]: http://sam.cat-v.org/