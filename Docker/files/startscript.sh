#VERSION 0.0.5
# service mysql restart
# /etc/init.d/mysql start

RESULT=`mysql -u root -p password --skip-column-names -e "SHOW DATABASES LIKE 'wala'"`
if [ "$RESULT" == "wala" ]; then
    echo "Database exist"
else
    echo "Database does not exist"
fi


cd walaintro
python app.py