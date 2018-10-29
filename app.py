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

if __name__ == '__main__':
	app.run(host=config.env['host'], port=config.env['port'], debug=True)