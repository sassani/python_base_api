# pylint: disable=no-name-in-module
"""User entity"""
import src.security.password_storage as ps
from database.context import DB
from index import APP_SETTINGS
from src.helpers.enums import Roles
from src.helpers.string_helpers import random_string


class User(DB.Model):
    """ User Model """
    id = DB.Column(DB.Integer, primary_key=True)
    public_id = DB.Column(DB.String(13))
    first_name = DB.Column(DB.String(80), unique=False, nullable=False)
    last_name = DB.Column(DB.String(80), unique=False, nullable=False)
    email = DB.Column(DB.String(120), unique=True, nullable=False)
    password = DB.Column(DB.String(120), unique=False, nullable=False)
    is_email_verified = DB.Column(DB.Boolean(1))
    is_active = DB.Column(DB.Boolean(1))
    roles = DB.Column(DB.JSON)


def seed():
    """ return entity seeds"""
    super_admin = User(
        public_id=random_string(13),
        first_name=APP_SETTINGS['supperAdmin']['firstName'],
        last_name=APP_SETTINGS['supperAdmin']['lastName'],
        email=APP_SETTINGS['supperAdmin']['email'],
        password=ps.generate_password(APP_SETTINGS['supperAdmin']['password']),
        roles={Roles.SUPER_ADMIN.name:None, Roles.ADMIN.name:None},
        is_email_verified=True,
        is_active=True
    )
    return super_admin
