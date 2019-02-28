""" Application enums """
from enum import Enum

class ApplicationType(Enum):
    """ Client types"""
    WEB = 1
    MOBILE = 2

class Roles(Enum):
    """ User Roles"""
    SUPER_ADMIN = 1
    ADMIN = 2
    READER = 3
    WRITER = 4

class LoginUserType(Enum):
    """ Login User type """
    CREDENTIALS = 1
    REFRESH_TOKEN = 2