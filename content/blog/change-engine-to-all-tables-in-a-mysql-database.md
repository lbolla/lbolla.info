---
categories:
  - "programming"
date: "2012-04-05"
description: "Change engine to all tables in a MySQL database"
tags:
  - "mysql"
title: "Change engine to all tables in a MySQL database"
---

Here is a simple shell script to change the engine of all the tables in a MySQL database:

    DBUSER=user
    DBPWD=password
    DBNAME=db
    ENGINE=MyISAM
    for t in `echo "show tables" | mysql -u$DBUSER -p$DBPWD --batch --skip-column-names $DBNAME`; do
        mysql -u$DBUSER -p$DBPWD $DBNAME -e "ALTER TABLE \`$t\` ENGINE = $ENGINE;";
    done

Just because, as usual, I keep forgetting these kind of things...
