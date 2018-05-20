all: html style push

html:
	emacs --eval '(org-publish-project "lbolla.info" t)'

style:
	curl http://gongzhitaao.org/orgcss/org.css -o static/css/org.css

push:
	rsync -acvz html/ lbolla.info:public2/

clean:
	rm -rf html/

.PHONY: org clean
