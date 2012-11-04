build: clean
	liquidluck build -v

server:
	liquidluck server

deploy: build
	cd _themes/momentum
	git pull
	cd ../..

clean: 
	rm -rf deploy
