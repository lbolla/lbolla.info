---
categories:
  - "programming"
date: "2011-09-26"
description: "There is more than one way to do it"
tags:
  - "haskell"
  - "http"
title: "HTTP client in Haskell"
---

To try to make sense of [this][1], I decided to write a "simple" http client in
Haskell in as many styles as I could think of:

    import Network.HTTP
    import Control.Applicative
    
    url = "http://www.haskell.org/haskellwiki/Haskell"
    
    --  Imperative style
    fetch_1 = do
        rsp <- Network.HTTP.simpleHTTP (getRequest url)
        body <- getResponseBody rsp
        return (take 1000 body)
    
    --  With Functors' fmap
    fetch_2 = do
        rsp <- Network.HTTP.simpleHTTP (getRequest url)
        fmap (take 1000) (getResponseBody rsp)
    
    --  With Applicative's >>=
    fetch_3 = fmap (take 1000) (Network.HTTP.simpleHTTP (getRequest url) >>= getResponseBody)
    
    --  "fmap f x" is the same as "pure f <*> x" (Applicative's law)
    fetch_4 = pure (take 1000) <*> (Network.HTTP.simpleHTTP (getRequest url) >>= getResponseBody)
    
    --  "pure f <*> x" is the same as "f <$> x"
    fetch_5 = (take 1000) <$> (Network.HTTP.simpleHTTP (getRequest url) >>= getResponseBody)

It's a long time since I found so many new concepts while studying a new programming language...

   [1]: http://learnyouahaskell.com/functors-applicative-functors-and-monoids
   [2]: http://hackage.haskell.org/packages/archive/HTTP/4000.0.9/doc/html/Network-HTTP-Base.html#t:Response
