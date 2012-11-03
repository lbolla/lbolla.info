# missing Dec_0 and friends from python decimal

- title: missing Dec_0 and friends from python decimal
- author: lbolla
- category: programming
- tags: decimal,Dec_0,Dec_n1,Dec_p1,python,undocumented
- summary: 
- post_id: 213
- date: 2010-07-29 12:05:31
- post_date_gmt: 2010-07-29 10:05:31
- comment_status: open
- post_name: missing-dec_0-and-friends-from-python-decimal
- status: publish
- post_type: post

----------------

This fails in py2.4, py2.5.1 and py2.6:
    
    from decimal import Dec_0
    
    

But it works in all the other py2.5 subversions!

It seems that exposing Dec_0 (and other similar constants) was considered a [bug][1] and "fixed" on Jan 3rd 2009 by renaming it `_Dec_0`.

Indeed, if I had looked at the source code, I would have seen that `Dec_0` was for "internal use only".

From `/usr/lib/python2.5/decimal.py:5159`
    
    ##### Useful Constants (internal use only) ################################
    
    # Reusable defaults
    Inf = Decimal('Inf')
    negInf = Decimal('-Inf')
    NaN = Decimal('NaN')
    Dec_0 = Decimal(0)
    Dec_p1 = Decimal(1)
    Dec_n1 = Decimal(-1)
    
    

Those definitions are missing in py2.4 and py2.5.1, and renamed in py2.6.

Damn: never use undocumented features!

   [1]: http://bugs.python.org/issue4812

## Comments

**[Emanuele Zattin](#73 "2010-07-29 13:23:51"):** Ma a che mai ti servirá?? :D

