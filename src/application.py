""" Main Application"""
import json
from flask import Flask, jsonify
from src.database import DB


def create_settings():
    """ global application settings"""
    settongs_file = 'appSettings.json'
    # if app.config['ENV'] == 'development':
    #     settongs_file = 'appSettings.json'

    return json.load(open(settongs_file))


def create_app(settings):
    """ Flask App"""
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = settings['database']['mySqlDsn']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route("/", methods=['GET'])
    def index():
        payload = {
            'Application': settings
        }
        return jsonify(payload)

    return app
