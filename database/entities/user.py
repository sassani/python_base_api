"""User entity"""
from index import APP_SETTINGS
from database.context import DB
from src.Helpers.enums import Roles
import src.security.password_storage as ps

class User(DB.Model):
    """ User Model """
    id = DB.Column(DB.Integer, primary_key=True)
    first_name = DB.Column(DB.String(80), unique=False, nullable=False)
    last_name = DB.Column(DB.String(80), unique=False, nullable=False)
    email = DB.Column(DB.String(120), unique=True, nullable=False)
    password = DB.Column(DB.String(120), unique=False, nullable=False)
    is_email_verified = DB.Column(DB.Boolean(1))
    is_active = DB.Column(DB.Boolean(1))
    roles = DB.Column(DB.JSON)

    def __repr__(self):
        return '<User %r>' % self.first_name

def seed():
    """ return entity seeds"""
    super_admin = User(
        first_name=APP_SETTINGS['supperAdmin']['firstName'],
        last_name=APP_SETTINGS['supperAdmin']['lastName'],
        email=APP_SETTINGS['supperAdmin']['email'],
        password=ps.generate_password(APP_SETTINGS['supperAdmin']['password']),
        roles={Roles.SUPER_ADMIN.name:None, Roles.ADMIN.name:None},
        is_email_verified=True,
        is_active=True
    )
    return super_admin
