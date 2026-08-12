---
title: Use Postgres advanced types in Python
date: 2013-03-06
tags:
- python
- programming
---
Postgres has a lot of useful [builtin data types](http://www.postgresql.org/docs/9.2/static/datatype.html), but only some of them are mapped to Python types when accessing the DB using [psycopg2](http://initd.org/psycopg/).

Extending the support to other types is not straightforward, and involves the following steps:

-   Create a Python class to store the data, e.g. `class Point`
-   Write a function to convert a `Point` to its SQL string representation, e.g. `adapt_point`
-   Write the inverse function to parse the SQL string representation of a `Point` and return and instance of a `Point`, e.g. `cast_point`
-   Finally bind all these functions and types, see `register_point_type`

The complete code is as follows, also available [as a gist](https://gist.github.com/lbolla/5098907):

<script src="https://gist.github.com/lbolla/5098907.js"></script>
