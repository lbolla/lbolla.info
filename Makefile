REMOTE_HOST="mylinode"
LL="/home/lbolla/.virtualenvs/lbolla.info/bin/liquidluck"

build: clean
	${LL} build -v

server:
	${LL} server

theme:
	cd _themes/momentum
	git pull
	cd ../..

deploy: build theme

remote:
	ssh ${REMOTE_HOST} "cd src/lbolla.info && git pull && make deploy"

clean: 
	rm -rf deploy
