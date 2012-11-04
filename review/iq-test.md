# IQ test

- title: IQ test
- author: lbolla
- category: italiano,programming
- tags: IQ programming python
- summary: 
- post_id: 60
- date: 2008-02-02 16:52:49
- post_date_gmt: 2008-02-02 14:52:49
- comment_status: open
- post_name: iq-test
- status: publish
- post_type: post

----------------

qualche giorno fa, mi sono imbattuto in questo [test di intelligenza][1], proposto da [ECM][2]. riporto il testo, per semplicita': 

> "Using each of the numbers 1, 2, 3, 4, 5, 6, 7, 8, 9 only once, form a nine digit number A that can satisfy the following criteria: - A is exactly divisible by 9. - Removing the rightmost digit from A forms an eight digit number B that is exactly divisible by 8. - Removing the rightmost digit from B forms a seven digit number C that is exactly divisible by 7. - Removing the rightmost digit from C forms a six digit number D that is exactly divisible by 6. - Removing the rightmost digit from D forms a five digit number E that is exactly divisible by 5. - Removing the rightmost digit from E forms a four digit number F that is exactly divisible by 4. - Removing the rightmost digit from F forms a three digit number G that is exactly divisible by 3. - Removing the rightmost digit from G forms a two digit number H that is exactly divisible by 2. What is A? Show how you produced B, C, D, E, F, G & H."

dopo un po', mi sono stufato, e ho prodotto questo. 
    
    
    def all_perms(str):
        if len(str) <=1:
            yield str
        else:
            for perm in all_perms(str[1:]):
                for i in range(len(perm)+1):
                    yield perm[:i] + str[0:1] + perm[i:]
    
    def list2num(p):
        y = 0
        d = len(p)
        for ip,pp in enumerate(p):
            y += 10**(d-ip-1) * pp
        return y
    
    def check(p):
        for i in xrange(1,len(p)-1):
            if list2num(p[:-i]) % (9-i) != 0:
                return False
        return True
    
    for p in all_perms(range(1,10)):
        if check(p):
            print p
            break

run it in python, of course!

   [1]: http://www.ecmselection.co.uk/high_iq_enter_and_win/brainbuster_no_25_-_remove_digits.html (IQ test)
   [2]: http://www.ecmselection.co.uk/ (ECM)