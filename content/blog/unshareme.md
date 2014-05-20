---
categories:
  - "programming"
date: "2012-12-12"
description: "Encrypt URLs so that they cannot be shared with others"
tags:
  - "go"
  - "web"
  - "hash"
title: "UnshareMe"
---

Last my weekend project was to write something similar to [WeHasLinks][2]. In
fact, [WeHasLinks][2] is a file sharing website, but I misread it as
"We-Hash-Links" and the funny thing is that they *indeed* hash their links (for
obvious reasons...). Anyway, [WeHasLinks][2]'s links are hashed so that only
the user who visited the page is allowed to them.

I liked the idea very much, and I decided to implement it in [go][4], as an
exercise!  You can find the code [on github][1]. A demo is available at
[unshareme.lbolla.info][3].

The links are encrypted using [AES-256][5] and validated using [HMAC][6], which
is the standard way to encrypt secure cookies in web apps. In fact,
[gorilla][7] provides a library to do just that. The code looks pretty much
like this:

    var hashKey = securecookie.GenerateRandomKey(32)
    var blockKey = securecookie.GenerateRandomKey(32)
    var encodeName = "encodeName"
    var sc = securecookie.New(hashKey, blockKey)
    ...

    func encode(msg PersonalURL) (string, error) {
        enc, err := sc.Encode(encodeName, msg)
        ...

"Personalization" of links is done coupling each link with the remote IP
visiting the page.

    // Store URI and IP together
    type PersonalURL struct {
        URI string
        IP string
    }

When visited, the web app will decode the link, verify that the remote IP
visiting it is the same as the IP who requested the links in the first place
and redirect to the *real* url. Otherwise, a 400 will be raised.

*Per se*, the app is very simple but I learnt a lot about [go][4] while
implementing itt: in particular, that in term of speed of development it's very
close to a scripting language [go][4]'s standard library is amazing and
[gorilla][8] is a very nice complement for web apps.

One thing I didn't like, is how [templates][9] are handled: it's overly
complicated to specify a relative path for the templates directory and
templates are not compiled into the source code automatically. The easiest
solution I found was to specify the path on the command line. In this case,
[10][yesod has a better solution].

Full code, for reference:

    package main

    import (
        "encoding/base64"
        "flag"
        "fmt"
        "github.com/gorilla/securecookie"
        "github.com/gorilla/mux"
        "html/template"
        "log"
        "net/http"
        "net/url"
        "path/filepath"
        "strings"
    )

    // Random stuff for encoding
    var hashKey = securecookie.GenerateRandomKey(32)
    var blockKey = securecookie.GenerateRandomKey(32)
    var encodeName = "encodeName"
    var sc = securecookie.New(hashKey, blockKey)

    // Router for handlers
    var router = mux.NewRouter()

    // Store URI and IP together
    type PersonalURL struct {
        URI string
        IP string
    }

    // Flags
    var templates_path = flag.String("t", "src/unshareme/tmpl/", "Path to the templates")
    var templates = template.New("")

    func encode(msg PersonalURL) (string, error) {
        enc, err := sc.Encode(encodeName, msg)
        if err != nil {
            return "", err
        }

        b64enc := base64.URLEncoding.EncodeToString([]byte(enc))

        return b64enc, nil
    }

    func decode(enc string) (msg PersonalURL, err error) {
        b64enc, err := base64.URLEncoding.DecodeString(enc)
        if err != nil {
            return
        }

        err = sc.Decode(encodeName, string(b64enc), &msg)
        if err != nil {
            return
        }

        return
    }

    // Only works for IPv4, like 127.0.0.1:12345, not IPv6 like [::1]:12345
    func remoteIP(r *http.Request) string {
        // Get it from headers, as set by nginx
        ip := r.Header.Get("X-Real-IP")
        if ip == "" {
            // Strips port number
            ip = strings.Split(r.RemoteAddr, ":")[0]
        }
    //         log.Print("IP:", ip)
        return ip
    }

    func MainHandler(w http.ResponseWriter, r *http.Request) {
        err := templates.ExecuteTemplate(w, "index.html", nil)
        if err != nil {
            http.Error(w, err.Error(), http.StatusInternalServerError)
        }
    }

    func EncodeHandler(w http.ResponseWriter, r *http.Request) {
        u, err := url.Parse(r.URL.Query().Get("u"))
        if err != nil {
            log.Print(err.Error())
            http.Error(w, "", http.StatusBadRequest)
            return
        }

        if u.Scheme == "" {
            http.Error(w, "Invalid scheme", http.StatusBadRequest)
            return
        }

        msg := PersonalURL{URI: u.String(), IP: remoteIP(r)}
        enc, err := encode(msg)
        if err != nil {
            log.Print(err.Error())
            http.Error(w, "", http.StatusBadRequest)
            return
        }

        link, _ := router.Get("Decode").URL("enc", enc)
        fmt.Fprint(w, link.String())
    }

    func DecodeHandler(w http.ResponseWriter, r *http.Request) {
        vars := mux.Vars(r)
        dec, err := decode(vars["enc"])
        if err != nil {
            log.Print(err.Error())
            http.Error(w, "", http.StatusBadRequest)
            return
        }

        if rip := remoteIP(r); dec.IP != rip {
            log.Print(dec.IP, rip)
            http.Error(w, "", http.StatusBadRequest)
            return
        }

        http.Redirect(w, r, dec.URI, http.StatusFound)
        return
    }

    func main() {
        flag.Parse()
        templates = template.Must(template.ParseFiles(filepath.Join(*templates_path, "index.html")))
        router.Handle("/favicon.ico", http.NotFoundHandler())
        router.HandleFunc("/", MainHandler).Methods("GET")
        router.HandleFunc("/enc", EncodeHandler).Methods("GET")
        router.HandleFunc("/dec/{enc}", DecodeHandler).Methods("GET").Name("Decode")
        http.Handle("/", router)
        log.Fatal(http.ListenAndServe(":7001", nil))
    }

   [1]: https://github.com/lbolla/unshareme
   [2]: http://wehaslinks.com/
   [3]: http://unshareme.lbolla.info/
   [4]: http://golang.org
   [5]: http://en.wikipedia.org/wiki/Advanced_Encryption_Standard
   [6]: http://en.wikipedia.org/wiki/Hash-based_message_authentication_code
   [7]: http://www.gorillatoolkit.org/pkg/securecookie
   [8]: http://www.gorillatoolkit.org/
   [9]: http://golang.org/pkg/html/template/
   [10]: http://www.yesodweb.com/book/shakespearean-templates
