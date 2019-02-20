""" Application context"""
from flask_sqlalchemy import SQLAlchemy

from index import APP

DB = SQLAlchemy(APP)

# pylint: disable=unused-import, wrong-import-position, no-member
import database.entities.user as user
import database.entities.application as application

DB.drop_all(bind=None)
DB.create_all()

DB.session.add(user.seed())
DB.session.add(application.seed())

DB.session.commit()
