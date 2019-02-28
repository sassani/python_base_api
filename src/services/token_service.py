""" Token Management"""
import jsons
import jwt

from index import APP_SETTINGS
from src.helpers.string_helpers import random_string
from src.helpers.error_handlers import ErrorHandlers as EH
from src.models.client import Client
from src.models.dtos import AccessTokenDto, AuthTokenDto
from src.models.user import User


class TokenService:
    """ Token creation and validation management """
    key = APP_SETTINGS['secretKey']

    def __init__(self,
                 user: User = None,
                 client: Client = None,
                 refresh_token: str = None
                 ):
        self.user = user
        self.client = client
        self.refresh_token = refresh_token
        if refresh_token is None:
            if user is not None and client is not None:
                self.refresh_token = self._generate_refresh_token()

    def generate_token(self, uclient_id: int) -> AuthTokenDto:
        """ create Authorization token """
        access_token = AccessTokenDto(self.user, uclient_id)
        encoded_token = jwt.encode(jsons.dump(access_token), self.key, 'HS256')
        auth_token = AuthTokenDto(
            str(encoded_token, 'utf-8'), self.refresh_token, self.user, 'bearer')
        return auth_token

    def _generate_refresh_token(self) -> str:
        """ create Refresh token """
        return str(self.user.id_) + \
            self.client.public_id + \
            random_string(32)

    def verify_token(self, token: str) -> AccessTokenDto:
        """ check token signature and expiration """
        decode_token = None
        token_str_parts = token.split(' ')
        if token_str_parts[0] == 'Bearer':
            token_str = token_str_parts[1]
            try:
                decode_token = jwt.decode(
                    token_str, self.key, algorithms=['HS256'])
            except jwt.exceptions.ExpiredSignatureError:
                raise EH(
                    'Token expired',
                    'Token has expired'
                )
            except jwt.exceptions.InvalidSignatureError:
                raise EH(
                    'Invalid signature',
                    'The signature of the token is invalid'
                )
            except jwt.exceptions.InvalidTokenError:
                raise EH(
                    'Invalid Token',
                    'Token is not valid'
                )
        return AccessTokenDto(decode_token)
