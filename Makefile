develop:
	docker run -v `pwd`:/app -w /app -t --rm -i my_youtuber /bin/bash

image:
	docker build -t my_youtuber .

clean:
	docker rmi my_youtuber
