docker run -p3306:3306 -e MYSQL_ROOT_HOST=172.17.0.1 -e MYSQL_ROOT_PASSWORD=password -e MYSQL_USER=root -d mysql/mysql-server

docker exec -it bdef75dfd47a mysql -uroot -ppassword

connect using 127.0.0.1

