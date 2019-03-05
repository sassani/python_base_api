# pylint: disable-msg=E0611
"""User entity"""

from src.database import DB
from src.core.models.client import Client
from src.core.helpers.error_handlers import ErrorHandlers as EH


class Login(DB.Model):
    """ User Client Model """
    id = DB.Column(DB.Integer, primary_key=True)
    client_id = DB.Column(DB.Integer)
    user_id = DB.Column(DB.Integer)
    refresh_token = DB.Column(DB.String(50))
    platform = DB.Column(DB.String(25))
    browser = DB.Column(DB.String(40))
    ip_add = DB.Column(DB.String(15))

    def add(self,
            client: Client = None,
            refresh: str = None,
            user_id: int = None
            ):
        """ insert user's to login table
            client has device info
        """
        if client is not None:
            self.client_id = client.id_
            self.platform = client.platform
            self.browser = client.browser
            self.ip_add = client.ip_
            self.refresh_token = refresh
            self.user_id = user_id
        DB.session.add(self)
        DB.session.commit()

    def logout_by_login_id(self, login_id: int):
        """ revoke login
            revoke user's refresh token
        """
        num_rows = Login.query.filter_by(id=login_id).delete()
        if num_rows == 0:
            raise EH(
                'User Already Logged Out',
                'No user from this machine is existed in our Data'
            )
        DB.session.commit()

    def logout_by_user_id(self, user_id: int, client_id: int = None):
        """ revoke all
            if client_id is not null    -> revoke user from all spesified application
            if client_id is null        -> revoke user completely (all application)
        """
        if client_id is not None:
            num_rows = Login.query.filter_by(
                user_id=user_id, client_id=client_id).delete()
            if num_rows == 0:
                raise EH(
                    'User Already Logged Out',
                    'No user from this app is existed in our Data'
                )

        else:
            num_rows = Login.query.filter_by(user_id=user_id).delete()
            if num_rows == 0:
                raise EH(
                    'User Already Logged Out',
                    'No user is existed in our Data'
                )
        DB.session.commit()
