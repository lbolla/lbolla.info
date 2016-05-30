---
categories:
  - "programming"
date: "2016-05-25"
description: "Implementing Elixir's pipe operator in Python"
tags:
  - "python"
  - "elixir"
title: "Elixir's pipe operator in Python"
---

[Elixir][1] implements lots of nice ideas, one of which is its [pipe operator][2]. It allows you to write things like:

    iex> [1, [2], 3] |> List.flatten()
    [1, 2, 3]

Or:

    iex> inc = fn x -> x + 1 end
    iex> dec = fn x -> x - 1 end
    iex> square = fn x -> x * x end
    iex> 5 |> inc.() |> dec.() |> square.()
    25

Today, just for fun, I tried to implement something similar in Python. Here is the result:

<script src="https://gist.github.com/lbolla/e7396c77e63b4c168cce27002f588494.js"></script>

So, you can write something like:

    >>> 5 |P| inc |P| dec |P| square
    25

Obviously, this is just a toy: it does not implement all the features available in the Elixir's one, but it was fun!

  [1]: http://elixir-lang.org
  [2]: http://elixir-lang.org/docs/stable/elixir/Kernel.html#%7C%3E/2
