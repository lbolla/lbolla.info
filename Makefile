HUGO=${GOPATH}/bin/hugo

run: clean
	${HUGO} server -w -s .

build: clean
	${HUGO} -s .

clean:
	rm -rf public/

push: build
	rsync -av --delete public/ lbolla.info:public/
