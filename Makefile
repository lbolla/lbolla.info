HUGO=${GOPATH}/bin/hugo
TEMPLATE=drafts/_template.md
EDITOR=emacsclient -n

run: clean
	${HUGO} server -w -s .

build:
	${HUGO} -s .

clean:
	rm -rf public/

push: build
	rsync -acv --delete public/ lbolla.info:public/

# Use as: make draft $POST=some_title.md
draft:
	cp ${TEMPLATE} drafts/${POST}
	${EDITOR} drafts/${POST}

# Use as: make new $POST=some_title.md
new:
	cp ${TEMPLATE} content/blog/${POST}
	${EDITOR} content/blog/${POST}
