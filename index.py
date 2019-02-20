""" Application entry point """
import json
from flask import Flask


APP_SETTINGS = json.load(open('appSettings.json'))

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = APP_SETTINGS['database']['mySqlDsn']


# pylint: disable=unused-import, wrong-import-position
import database.context
import src.Controllers.routes
