# from sqlalchemy import Column, Integer, Sequence, String, create_engine
# from db.database import Database

# class User(Base):
print('---> User imported')

class User():
    # pass
    persist = [
        {'firstname':'Integer,15'},
        {'lastname':'String,15'},
        {'email':'String,15'},
        {'password':'String,15'},
    ]
    # __tablename__ = 'users'
    # id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    # firstname = Column(String(15))
    # lastname = Column(String(15))
    # email = Column(String(15))
    # password = Column(String(15))
    # session = Database.session
    # firstname = ''
    # lastname = ''
    # email = ''
    # password = ''

    def __init__(self, firstname, lastname, email, password):
        # super().__init__('users')
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        # self.migrate()
    
    @property
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

# Database.Base
# Database.base.metadata.create_all(Database.engine)
    
