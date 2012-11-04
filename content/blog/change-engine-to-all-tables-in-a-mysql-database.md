# Change engine to all tables in a MySQL database

- author: lbolla
- category: programming
- tags: mysql
- summary: Change engine to all tables in a MySQL database
- date: 2012-04-05 16:53:57

----------------

Here is a simple shell script to change the engine of all the tables in a MySQL database:

    DBUSER=user
    DBPWD=password
    DBNAME=db
    ENGINE=MyISAM
    for t in `echo "show tables" | mysql -u$DBUSER -p$DBPWD --batch --skip-column-names $DBNAME`; do
        mysql -u$DBUSER -p$DBPWD $DBNAME -e "ALTER TABLE \`$t\` ENGINE = $ENGINE;";
    done

Just because, as usual, I keep forgetting these kind of things...

## Comments

**[Andre](#921 "2012-10-10 22:19:51"):** Thank you, Works great!

