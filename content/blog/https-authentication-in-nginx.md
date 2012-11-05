# HTTPS authentication in nginx

- author: lbolla
- category: programming
- tags: http
- summary: 
- date: 2012-02-20 13:20:29

----------------

In order not to forget again how to setup [http authentication][1] in
[nginx][2] here is a reminder.

For `HTTPS` follow [these steps][3]:
    
    $ sudo -s
    # cd /etc/nginx
    # openssl req -new -x509 -nodes -out server.crt -keyout server.key
    

and add these lines to your `server` instance: 
    
    server {
        listen 443;
        ssl                  on;
        ssl_certificate      /etc/nginx/server.crt;
        ssl_certificate_key  /etc/nginx/server.key;
    ...
    

To setup basic authentication, add these lines to the same file:
    
    location / {
        auth_basic "Restricted";
        auth_basic_user_file /etc/nginx/htpasswd;
        # you might also want to deny access based on IP here
        #allow <ip-address>;
        #deny all;
    ...
    

Finally, to generate `/etc/nginx/htpasswd`, use this one-liner:
    
    echo -e "your-username:`perl -le 'print crypt("your-password","salt")'`" > /etc/nginx/htpasswd
    
Restart `nginx` and [Bob's your uncle][4]!

   [1]: http://en.wikipedia.org/wiki/Basic_access_authentication
   [2]: http://nginx.org/
   [3]: http://dracoblue.net/dev/https-nginx-with-self-signed-ssl-certificate/188/
   [4]: http://en.wikipedia.org/wiki/Bob's_your_uncle