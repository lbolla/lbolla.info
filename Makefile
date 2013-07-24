REMOTE_HOST="mylinode"
LL="${HOME}/.virtualenvs/lbolla.info/bin/liquidluck"

all: build

prerequisite:
	git submodule add git@github.com:lbolla/liquidluck-theme-moment.git _themes/momentum
	pip install liquidluck tornado

build: clean
	${LL} build -v

server:
	${LL} server

theme:
	cd _themes/momentum && git checkout momentum && git pull && cd ../..

deploy: theme build

remote:
	ssh ${REMOTE_HOST} "cd src/lbolla.info && git checkout liquidluck && git pull && make deploy"

clean: 
	rm -rf deploy
