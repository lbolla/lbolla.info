# http client in haskell

- title: http client in haskell
- author: lbolla
- category: programming
- tags: client,functional,haskell,http
- summary: 
- post_id: 297
- date: 2011-09-26 15:05:28
- post_date_gmt: 2011-09-26 15:05:28
- comment_status: open
- post_name: http-client-in-haskell
- status: publish
- post_type: post

----------------

To try to make sense of [this][1], I decided to write a "simple" http client in Haskell in as many styles as I could think of:

[haskell] import Network.HTTP import Control.Applicative url = "http://www.haskell.org/haskellwiki/Haskell" -- Imperative style fetch_1 = do rsp <- Network.HTTP.simpleHTTP (getRequest url) body <- getResponseBody rsp return (take 1000 body) -- With Functors' fmap fetch_2 = do rsp <- Network.HTTP.simpleHTTP (getRequest url) fmap (take 1000) (getResponseBody rsp) -- With Applicative's >>= fetch_3 = fmap (take 1000) (Network.HTTP.simpleHTTP (getRequest url) >>= getResponseBody) -- "fmap f x" is the same as "pure f <*> x" (Applicative's law) fetch_4 = pure (take 1000) <*> (Network.HTTP.simpleHTTP (getRequest url) >>= getResponseBody) -- "pure f <*> x" is the same as "f <$> x" fetch_5 = (take 1000) <$> (Network.HTTP.simpleHTTP (getRequest url) >>= getResponseBody) [/haskell] 

it's a long time since I found so many new concepts while studying a new programming language...

   [1]: http://learnyouahaskell.com/functors-applicative-functors-and-monoids

## Comments

**[jacques](#930 "2012-10-16 20:32:27"):** How do I get the response-code (int) i.e 200,404 in any of those ?

**[lbolla](#931 "2012-10-17 09:17:26"):** You can use `rspCode` on the response: [rspCode][1].

   [1]: http://hackage.haskell.org/packages/archive/HTTP/4000.0.9/doc/html/Network-HTTP-Base.html#t:Response

