# Year 2038 bug in MySQL

- author: lbolla
- category: programming
- tags: mysql
- summary: 
- date: 2011-03-04 16:35:43

----------------

Today I hit the ["year 2038" bug][1]. While working on MySQL, I did something like: 
    
    mysql> create table y2038 (x timestamp);
    
    mysql> insert into y2038 values ('1900-01-01');
    Query OK, 1 row affected, 1 warning (0.04 sec)
    
    mysql> insert into y2038 values ('2050-01-01');
    Query OK, 1 row affected, 1 warning (0.04 sec)
    
    mysql> select * from y2038;
    +---------------------+
    | x                   |
    +---------------------+
    | 0000-00-00 00:00:00 |
    | 0000-00-00 00:00:00 |
    +---------------------+
    2 row in set (0.00 sec)
    
    mysql> drop table y2038; -- damn
    

[It turned out][2] that MySQL's `TIMESTAMP` only accepts dates between
`1970-01-01 00:00:01` and `2038-01-19 03:14:07`: everything outside this range
will be truncated.

At least, it will not be called ["Friday the 13th" bug][1]!

Use `DATETIME` instead! And [RTFM][3] before doing anything!

   [1]: http://2038bug.com/
   [2]: http://dev.mysql.com/doc/refman/5.0/en/datetime.html
   [3]: http://a8888emfzelkaw4avz1gqr8s7y.hop.clickbank.net/

## Comments

**[Mark](#88 "2011-03-04 16:41:49"):** Or a better database.

