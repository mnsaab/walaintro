from flask import *
import os
import config
import controllers
import api
import extensions

app = Flask(__name__, template_folder="templates")

app.register_blueprint(api.app, url_prefix='/walaApp')
app.register_blueprint(controllers.home, url_prefix='/walaApp')

app.secret_key = os.urandom(25)
host = os.getenv('MYSQL_HOST', config.env['host'])
port = os.getenv('MYSQL_PORT', config.env['port'])
print(host, port)
if __name__ == '__main__':
	app.run(debug=True)