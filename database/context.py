""" Application context"""
from flask_sqlalchemy import SQLAlchemy

from index import APP

DB = SQLAlchemy(APP)

# pylint: disable=unused-import, wrong-import-position, no-member, no-name-in-module
import database.entities.user as user
import database.entities.client as client
import database.entities.login as login

DB.drop_all(bind=None)
DB.create_all()

DB.session.add(user.seed())
DB.session.add(client.seed())

DB.session.commit()
