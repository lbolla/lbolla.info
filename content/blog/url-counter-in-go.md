# URL Counter in GO

- author: lbolla
- category: programming
- tags: go, google
- summary: 
- date: 2012-10-10 14:33:56

----------------

After having [tinkered with Haskell for quite a bit][1], I decided that I
needed some rest from theory and esoteric concepts, and a more pragmatic
programming language to explore.

I've spent the last few days refreshing my memories on [Go][2]: I hadn't
touched it for almost 2 years and I must say that I find it changed: for the
better.

Here is a short tutorial on how to write a simple web application in Go, and
publish it on [Google App Engine][3]. The application is not a mere exercise,
but scratches an itch I recently had: it counts how many times each of its
handlers is hit. So, for example, visiting:
<http://go-count-urls.appspot.com/hello> returns how many times the `/hello`
handler has been visited. You can use it as a trivial real-time tracker.

For example, I used it to verify that an email I sent to someone was actually
opened (and presumably read). I just picked a random URL path (like
<http://go-count-urls.appspot.com/random-string-here>) and created an html
email with an empty `img` tag pointing to it: `<img
src="http://go-count-urls.appspot.com/random-string-here" width=0 height=0 />`.
Every time the email client opens the email, it requires that URL and the hit
is recorded. I admit that this use is pretty lame, and that there are [other
services][4] doing this, but I needed a real-world problem to work on!

So here we go! 

## Setup your development environment

First of all, download and install the [App Engine Go software development kit][5]. Then create the following directory structure: 
    
    go-count-urls/
        app.yaml
        app/
            counter.go

## Show me the code!

The whole application is made of just one file `[counter.go`][6]. Here it is, comments inline:

    package counter
    import (
        "appengine"
        "appengine/datastore"
        "fmt"
        "net/http"
        "time"
    )
     
    // Object to store in Google's Datastore. Keeps track of how many times a
    // URL was hit and when.
    type Counter struct {
        Path      string
        Count     int
        Timestamp time.Time
    }
     
    // Return a brand new Counter
    func getEmptyCounter(path string) Counter {
        return Counter{Path: path, Count: 0, Timestamp: time.Now()}
    }
     
    // Increment the counter for a URL. If it's the first time this URL is
    // visited, create a brand new Counter before incrementing it.
    // On error, return and empty counter and an error.
    func inc(c appengine.Context, key *datastore.Key, path string) (Counter, error)
    {
        var x Counter
     
        if err := datastore.Get(c, key, &amp;x); err != nil &amp;&amp; err !=
    datastore.ErrNoSuchEntity {
            return getEmptyCounter(path), err
        }
     
        // Increment it, and update the last modified time
        x.Path = path
        x.Count++
        x.Timestamp = time.Now()
     
        // Save the counter
        if _, err := datastore.Put(c, key, &amp;x); err != nil {
            return getEmptyCounter(path), err
        }
     
        return x, nil
    }
     
    // This is the only handler. It just picks the paths, removed the leading
    // slash and stores it in the Datastore. As a key in the Datastore, the URL
    // itself is used.
    func handle(w http.ResponseWriter, r *http.Request) {
     
        key := r.URL.Path[1:]
        if key == "" {
            // Return 404 on the root handler (we might want a splash page here...)
            http.NotFound(w, r)
            return
        } else if key == "favicon.ico" {
            // We are not interested in tracking favicon.ico
            w.WriteHeader(http.StatusNoContent)
            return
        }
     
        c := appengine.NewContext(r)
     
        // For how to use the Datastore see
    https://developers.google.com/appengine/docs/go/datastore/overview
        count, err := inc(c, datastore.NewKey(c, key, "singleton", 0, nil),
    r.URL.Path)
        if err != nil {
            http.Error(w, err.Error(), http.StatusInternalServerError)
            return
        }
     
        // Write something
        w.Header().Set("Content-Type", "text/plain; charset=utf-8")
        fmt.Fprintf(w, "Path=%s, Count=%d, When=%s", count.Path, count.Count,
    count.Timestamp)
    }
     
    // Initialize the application, binding URLS to handlers.
    func init() {
        http.HandleFunc("/", handle)
    }

## Try it out!

Launch the application using the SDK; from go-count-urls directory type: 
    
     $> $GAE_PATH/dev_appserver.py . 

Now visit <http://localhost:8080/hello>. Refresh. Refresh again. And again... 

## Publish

Publishing the application on Google infrastructure is a matter of seconds: 
    
     $> $GAE_PATH/appcfg.py update . 

You can visit it at: <http://go-count-urls.appspot.com/hello>. The code is available here: <https://github.com/lbolla/go-count-urls>.

   [1]: http://lbolla.info/blog/tag/haskell/
   [2]: http://golang.org/
   [3]: https://developers.google.com/appengine/
   [4]: http://www.spypig.com/
   [5]: https://developers.google.com/appengine/docs/go/gettingstarted/devenvironment
   [6]: https://github.com/lbolla/go-count-urls/blob/master/app/counter.go
