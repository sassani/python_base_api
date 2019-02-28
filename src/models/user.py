# pylint: disable-msg=E0611
from database.entities.user import User as UserDb

class User():
    def __init__(self, user_db: UserDb, current_login_id: int = None):
        self.id_: int = user_db.id
        self.pid: str = user_db.public_id
        self.first_name: str = user_db.first_name
        self.last_name: str = user_db.last_name
        self.email: str = user_db.email
        self.roles: object = user_db.roles
        self.is_active: bool = user_db.is_active
        self.is_verified: bool = user_db.is_email_verified
        self.current_login_id = current_login_id
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)    
