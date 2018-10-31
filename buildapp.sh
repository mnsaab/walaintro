docker build . -t walaintro --no-cache

docker run walaintro:latest -e MYSQL_HOST=localhost -e MYSQL_PORT=3306