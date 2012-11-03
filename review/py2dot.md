# py2dot

- title: py2dot
- author: lbolla
- category: 
- tags: 
- summary: 
- post_id: 72
- date: 2008-10-04 19:07:09
- post_date_gmt: 2008-10-04 17:07:09
- comment_status: open
- post_name: py2dot
- status: trash
- post_type: page

----------------

[caption id="attachment_78" align="alignnone" width="543" caption="py2dot.py -r1 -i -f examples/classes/complicated.py | fdp -Tpng -o complicated.png"]![py2dot.py -r1 -i -f examples/classes/complicated.py | fdp -Tpng -o complicated.png][1][/caption] 

[py2dot][2] is a python script to generate a dot file from a python script. the above picture is a typical py2dot output, from one of the example files available in the distribution. functions are represented by ellipsis, arrows represent function calls, classes are in dashed boxes and imported files in gray boxes. the output dot file can be viewed with a program liken [graphviz][3]. [py2dot is available from pypi][4]. documentation is available [here][5]. 

   [1]: http://lbolla.info/blog/wp-content/uploads/2008/10/complicated1.png
   [2]: http://pypi.python.org/pypi/py2dot/ (py2dot)
   [3]: http://www.graphviz.org/ (graphviz)
   [4]: http://pypi.python.org/pypi/py2dot (py2dot)
   [5]: http://packages.python.org/py2dot/ (py2dot doc)