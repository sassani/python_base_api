import os

import sqlalchemy
from sqlalchemy import Column, Integer, Sequence, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.user import User

print('---> Database imported')

Base = declarative_base()
tablename='default value'
engine = create_engine(os.getenv('MYSQL_DSN'))
Session = sessionmaker(bind=engine)
session = Session()
# base = Base




class Model(Base):
	__tablename__ = 'tablename'
	id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
	name = Column(String(15))
	fullname = Column(String(15))
	password = Column(String(15))
	address = Column(String(15))


print(User.persist[0].keys())
print(User.persist[0].values())
# Base.metadata.create_all(engine)

# def __init__(self, tablename):
# 	print(tablename)
# 	self.__tablename__ = tablename


# 	def __repr__(self):
# 	    return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password, self.address)
# @classmethod
# def migrate(cls):
# 	print('Migrate --->',cls.tablename)
# 	# Base.metadata.create_all(self.engine)

# 
