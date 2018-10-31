import MySQLdb
import MySQLdb.cursors
import config
import os

def connect_to_database():
	host = os.getenv('MYSQL_HOST', config.env['host'])
	options = {
		'host': host,
		'user': config.env['user'],
		'passwd': config.env['password'],
		'db': config.env['db'],
		'cursorclass': MySQLdb.cursors.DictCursor
	}

	db = MySQLdb.connect(**options)
	db.autocommit(True)
	return db

db = connect_to_database()