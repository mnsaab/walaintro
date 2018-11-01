docker build . -t walaintro --no-cache

docker run walaintro:latest -e MYSQL_HOST=127.0.0.1 -e MYSQL_PORT=3306