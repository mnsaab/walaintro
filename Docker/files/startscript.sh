#VERSION 0.0.4
# service mysql restart
# /etc/init.d/mysql start

# RESULT=`mysql -u root --skip-column-names -e "SHOW DATABASES LIKE 'wala'"`
# if [ "$RESULT" == "wala" ]; then
#     echo "Database exist"
# else
#     echo "Database does not exist"
# fi


cd walaintro
python app.py