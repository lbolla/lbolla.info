all: html style push

html:
	emacs --eval '(org-publish-project "lbolla.info" t)'

style:
	curl http://gongzhitaao.org/orgcss/org.css -o static/css/org.css

push:
	rsync -acvz html/ lbolla.info:public2/

org:
	mkdir -p org
	bin/md2org.sh
	sed -i 's/\[\[\/blog\//\[\[/g' org/*.org

clean:
	rm -rf html/

.PHONY: org clean
