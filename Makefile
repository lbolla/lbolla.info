REMOTE_HOST="mylinode"
LL="${HOME}/.virtualenvs/lbolla.info/bin/liquidluck"

build: clean
	${LL} build -v
	mv deploy/feed.html deploy/feed.xml

server:
	${LL} server

theme:
	cd _themes/momentum && git checkout momentum && git pull && cd ../..

deploy: theme build

remote:
	ssh ${REMOTE_HOST} "cd src/lbolla.info && git checkout liquidluck && git pull && make deploy"

clean: 
	rm -rf deploy
