# Editors' speed on opening big files

- author: lbolla
- category: programming
- tags: ed, sam, vim
- summary: How quick are common editors in opening big files?
- date: 2010-05-17 15:05:47

----------------

While playing with different editors (namely [vim][1] and [sam][2]) I tried to
time how long some common editors take to open a big file (~140Mb).

Here are the results:

<table>
<tr>
<th>editor</th>
<th>real</th>
<th>user</th>
<th>sys</th>
</tr>
<tr>
<td>`ed`</td>
<td>4.866s</td>
<td>3.440s</td>
<td>3.440s</td>
</tr>
<tr>
<td>`vim`</td>
<td>2.086s</td>
<td>0.836s</td>
<td>0.232s</td>
</tr>
<tr>
<td>`nano`</td>
<td>16.264s</td>
<td>15.361s</td>
<td>0.172s</td>
</tr>
<tr>
<td>`sam`</td>
<td colspan="3">way too long</td>
</tr>
</table>

Then, for curiosity, I timed `less` with and without (`-n`) line numbering:

<table>
<tr>
<td>`less`</td>
<td>3.552s</td>
<td>0.200s</td>
<td>0.072s</td>
</tr>
<tr>
<td>`less -n`</td>
<td>0.182s</td>
<td>0.016s</td>
<td>0.016s</td>
</table>

Not sure what to do with these numbers, yet...

   [1]: http://www.vim.org
   [2]: http://sam.cat-v.org/
