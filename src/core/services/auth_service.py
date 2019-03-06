# pylint: disable-msg=E0611, ungrouped-imports
""" authentication and Authorization services"""

import src.core.security.password_storage as ps
from src.database.user import User as UserDb
from src.database.login import Login as LoginDb
from src.core.helpers.enums import LoginUserType
from src.core.models.client import Client
from src.core.models.dtos import AuthTokenDto, LoginUserDto
from src.core.models.user import User
from src.core.services.token_service import TokenService


class AuthService():
    """ Authenticate"""

    def __init__(self, login_user: LoginUserDto = None):
        self.authenticated_user: User = None
        self.login_db: LoginDb = None
        self.token_service: TokenService = None
        if login_user is not None:
            self.login_user: LoginUserDto = login_user

    def authenticate(self) -> bool:
        """ Authenticate user by email-password or refreshToken"""
        user_db = None

        if self.login_user.type is LoginUserType.CREDENTIALS:
            user_db = UserDb.query.filter_by(
                email=self.login_user.email).first()
        elif self.login_user.type is LoginUserType.REFRESH_TOKEN:
            self.login_db = LoginDb.query.filter_by(
                refresh_token=self.login_user.refresh_token).first()
            if self.login_db:
                user_db = UserDb.query.filter_by(
                    id=self.login_db.user_id).first()

        if user_db:
            self.authenticated_user = User(user_db)
            if self.login_user.type is LoginUserType.CREDENTIALS:
                if not ps.verify_password(self.login_user.password, user_db.password):
                    return False
            return True
        return False

    def token(self, client: Client) -> AuthTokenDto:
        """ return Authentication token"""
        if self.login_user.type is LoginUserType.CREDENTIALS:
            self.token_service = TokenService(self.authenticated_user, client)
            self._login(client)
        else:
            self.token_service = TokenService(
                self.authenticated_user, client, self.login_db.refresh_token)

        return self.token_service.generate_token(self.login_db.id)

    def _login(self, client: Client) -> bool:
        """ add user client data """
        self.login_db = LoginDb()
        self.login_db.add(client,
                          self.token_service.refresh_token,
                          self.authenticated_user.id_)

    def authorize(self, token: str):
        """ create user object by verified token """
        access_token = TokenService().verify_token(token)
        user_db = user_db = UserDb.query.filter_by(id=access_token.uid).first()
        if user_db:
            self.authenticated_user = User(user_db, access_token.aid)

    def logout(self, login_id: int):
        """ revoke login
            revoke user's refresh token
        """
        login_db = LoginDb()
        login_db.logout_by_login_id(login_id)
