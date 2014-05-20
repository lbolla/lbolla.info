---
categories:
  - "programming"
date: "2013-08-28"
description: "Reminder on how to connect to MSSQL servers from Python"
tags:
  - "python"
  - "mssql"
  - "odbc"
  - "freetds"
title: "Connect to MSSQL from Python with ODBC and FreeTDS"
---

This is another of those posts that I wrote because I always forget how to do
things...

This time, I don't want to forget how to connect from Python to MSSQL server
anymore. In order to do it, you need the following system packages installed:

    $> sudo apt-get install unixodbc-dev tdsodbc sqsh

`sqsh` installs all the required `freetds`-related  libraries; `tdsodbc` is the
[FreeTDS][3] driver for [ODBC][2] and `unixodbc-dev` is needed to install
[`pyodbc`][1].

Then install `pyodbc` using `pip` or whatever else you like:

    $> pip install pyodbc

Finally, the tricky part. You need 3 config files:

* `/etc/freetds/freetds.conf`: this stores the configuration for the
  endpoints to MSSQL servers
* `/etc/odbcinst.ini`: this defines the driver that ODBC uses. In fact, it
  mentiones the `FreeTDS` shared libraries installed with the system
  package `tdsodbc`. Edit to match your system.
* `$HOME/.odbc.ini`: finally, this file defines the database, username and
  password to connect to and the driver to use.

Files are available on `gist`.

<script src="https://gist.github.com/lbolla/6364001.js"></script>

Now you can connect using [`pyodbc`][1] using something like this:

    CONNECTION = pyodbc.connect(
        'DRIVER=FreeTDS;'
        'SERVER=mssql-host;'
        'PORT=1433;'
        'DATABASE=dbname;'
        'UID=username;'
        'PWD=password;'
        'CHARSET=UTF-8;'
        'TDS_Version=8.0')

   [1]: https://code.google.com/p/pyodbc/
   [2]: http://en.wikipedia.org/wiki/ODBC
   [3]: http://en.wikipedia.org/wiki/FreeTDS
   [4]: https://gist.github.com/lbolla/6364001
