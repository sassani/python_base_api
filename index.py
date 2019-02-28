""" Application entry point """
import json
from flask import Flask


APP = Flask(__name__)
APP_SETTINGS_FILE = 'appSettings.json'
if APP.config['ENV'] == 'development':
    APP_SETTINGS_FILE = 'appSettings.dev.json'

APP_SETTINGS = json.load(open(APP_SETTINGS_FILE))

APP.config['SQLALCHEMY_DATABASE_URI'] = APP_SETTINGS['database']['mySqlDsn']
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# pylint: disable=unused-import, wrong-import-position, E0611
import database.context
import src.controllers.routes
