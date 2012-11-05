REMOTE_HOST="mylinode"
LL="/home/lbolla/.virtualenvs/lbolla.info/bin/liquidluck"

build: clean
	${LL} build -v

server:
	${LL} server

deploy: build
	cd _themes/momentum
	git pull
	cd ../..

remote:
	ssh ${REMOTE_HOST} "cd src/lbolla.info && git pull && make build"

clean: 
	rm -rf deploy
