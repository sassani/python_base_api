""" DTO Models """
# from typing import NamedTuple
# from collections import namedtuple


# class LoginUserDto(NamedTuple):
class LoginUserDto:
    """ Login User DTO """

    def __init__(self, jsonObject):
        self.client_id = jsonObject['clientId']
        self.email = jsonObject['email']
        self.password = jsonObject['password']
