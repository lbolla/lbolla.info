# Change engine to all tables in a MySQL database

- title: Change engine to all tables in a MySQL database
- author: lbolla
- category: programming
- tags: alter table,batch,engine,mysql
- summary: 
- post_id: 397
- date: 2012-04-05 16:53:57
- post_date_gmt: 2012-04-05 15:53:57
- comment_status: open
- post_name: change-engine-to-all-tables-in-a-mysql-database
- status: publish
- post_type: post

----------------

Here is a simple shell script to change the engine of all the tables in a MySQL database:
    [code lang="shell"]#!/bin/sh
    DBUSER=user
    DBPWD=password
    DBNAME=db
    ENGINE=MyISAM
    for t in `echo "show tables" | mysql -u$DBUSER -p$DBPWD --batch --skip-column-names $DBNAME`; do
    mysql -u$DBUSER -p$DBPWD $DBNAME -e "ALTER TABLE \`$t\` ENGINE = $ENGINE;";
    done
    [/code]
    Just because, as usual, I keep forgetting these kind of things...

## Comments

**[Andre](#921 "2012-10-10 22:19:51"):** Thank you, Works great!

