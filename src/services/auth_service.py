""" authentication and Authorization services"""
from src.models.dtos import LoginUserDto
from database.entities.user import User
import src.security.password_storage as ps


class AuthService():
    """ Authenticate"""
    def __init__(self, login_user: LoginUserDto):
        self.login_user = login_user
    
    def authenticate(self):
        result = False
        user = User.query.filter_by(email=self.login_user.email).first()
        if(user):
            if(ps.verify_password(self.login_user.password,user.password)):
                result = True

        return result
