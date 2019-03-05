from src.database.client import Client as ClientDb


class Client():
    def __init__(self, client_db: ClientDb = None):
        if client_db is not None:
            self.id_ = client_db.id
            self.public_id = client_db.public_id
            self.secret = client_db.secret
            self.type = client_db.type
            self.is_valid = True
            self.browser = None
            self.platform = None
            self.ip_ = None
        else:
            self.is_valid = False

    def set_session_info(self, browser: str, platform: str, ip: str):
        self.browser = browser
        self.platform = platform
        self.ip_ = ip
