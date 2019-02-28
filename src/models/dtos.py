""" DTO Models """
import datetime
from src.models.user import User
from src.helpers.enums import LoginUserType

# pylint: disable=invalid-name


class LoginUserDto:
    """ Login User DTO """

    def __init__(self, jsonObject):
        if jsonObject is not None:
            self.is_valid = False

            self.client_id = jsonObject.get('clientId')
            self.client_secret = jsonObject.get('clientSecret')
            self.email = jsonObject.get('email')
            self.password = jsonObject.get('password')
            self.refresh_token = jsonObject.get('refreshToken')
            if self.client_id:
                self.is_valid = True
                if self.email and self.password:
                    self.type = LoginUserType.CREDENTIALS
                elif self.refresh_token:
                    self.type = LoginUserType.REFRESH_TOKEN
                else:
                    self.is_valid = False


class AuthTokenDto:
    """ Authentication Token DTO"""

    def __init__(self, access_token: str, refresh_token: str, user: User, token_type: str):
        self.accessToken = access_token
        self.refreshToken = refresh_token
        self.pid = user.pid
        self.roles = user.roles
        self.tokenType = token_type
        self.is_verified = user.is_verified


class AccessTokenDto:
    """ Access Token DTO"""

    def __init__(self, user: User or object, uclient_id: int = None):
        if uclient_id is not None:
            self.aid = uclient_id
            self.uid = user.id_
            self.exp = datetime.datetime.now().timestamp() + 3 * 3600
            self.roles = user.roles
        else:
            self.aid = user['aid']
            self.exp = None
            self.uid = user['uid']
            self.roles = user['roles']
