#VERSION 0.0.2
FROM ubuntu:17.10
ENV NPM_CONFIG_LOGLEVEL info

RUN apt-get update -qq
RUN apt-get install -y libmysqlclient-dev

ARG DEBIAN_FRONTEND="noninteractive" 
RUN apt-get install -y mysql-server 

RUN apt-get install -y python 
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install flask mysqlclient

RUN apt-get install -y git

RUN git clone https://github.com/mnsaab/walaintro.git
COPY files/startscript.sh /root/startscript.sh
RUN chmod +x /root/startscript.sh 
RUN chmod -R 755 /var/lib/mysql/
ENTRYPOINT ["bash", "/root/startscript.sh"]
