HUGO=${GOPATH}/bin/hugo

run: clean
	${HUGO} server -w -s .

build:
	${HUGO} -s .

clean:
	rm -rf public/

push: build
	rsync -acv --delete public/ lbolla.info:public/
