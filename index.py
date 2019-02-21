""" Application entry point """
import json
from flask import Flask


APP = Flask(__name__)
app_setting_file = 'appSettings.json'
if APP.config['ENV'] == 'development':
    app_setting_file = 'appSettings.dev.json'

APP_SETTINGS = json.load(open(app_setting_file))

APP.config['SQLALCHEMY_DATABASE_URI'] = APP_SETTINGS['database']['mySqlDsn']
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# pylint: disable=unused-import, wrong-import-position
import database.context
import src.Controllers.routes
