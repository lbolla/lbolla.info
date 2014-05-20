---
categories:
  - "programming"
date: "2013-03-06"
description: "How to use Postgres types with SQLAlchemy"
tags:
  - "postgres"
  - "sqlalchemy"
  - "python"
  - "psycopg2"
title: "Use Postgres advanced types in Python"
---

Postgres has a lot of useful [builtin data types][1], but only some of them are
mapped to Python types when accessing the DB using [psycopg2][2].

Extending the support to other types is not straightforward, and involves the
following steps:

   * Create a Python class to store the data, e.g. `class Point`
   * Write a function to convert a `Point` to its SQL string representation,
     e.g. `adapt_point`
   * Write the inverse function to parse the SQL string representation of a
     `Point` and return and instance of a `Point`, e.g. `cast_point`
   * Finally bind all these functions and types, see `register_point_type`

The complete code is as follows, also available [as a gist][3]:

<script src="https://gist.github.com/lbolla/5098907.js"></script>


   [1]: http://www.postgresql.org/docs/9.2/static/datatype.html
   [2]: http://initd.org/psycopg/
   [3]: https://gist.github.com/lbolla/5098907
