from flask import request

from src.database.client import Client as ClientDb
from src.core.helpers.enums import ApplicationType
from src.core.models.client import Client
from src.core.models.dtos import LoginUserDto


class ClientService():

    def __init__(self, login_user: LoginUserDto):
        self.client = Client()
        self.set_client(login_user)
        self.set_session_info()

    def set_client(self, login_user: LoginUserDto):
        """ validate requested client and set client object """
        if(not login_user.is_valid):
            # TODO: create error handler for bad dto
            return None
        client_db = ClientDb.query.filter_by(
            public_id=login_user.client_id).first()
        if(client_db):
            if(client_db.type != ApplicationType.WEB):
                # TODO: check client secret and return None if it is invalid
                pass
            self.client = Client(client_db)

    def set_session_info(self):
        ua_string = request.user_agent.string.split(' ', 1)[0]
        browser = ua_string + (' ' + request.user_agent.browser if request.user_agent.browser else '')
        platform = request.user_agent.platform
        ip_add = request.remote_addr
        self.client.set_session_info(browser, platform, ip_add)
