build: clean
	liquidluck build -v

server:
	liquidluck server

clean: 
	rm -rf deploy
