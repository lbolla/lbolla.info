HUGO=${GOPATH}/bin/hugo

run:
	${HUGO} server -w -s .

build:
	${HUGO} -s .

push:
	rsync -av --delete public/ lbolla.info:public/
