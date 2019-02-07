from models.user import User
# from models.project import Project
# import sqlalchemy
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine, Column, Integer, String, Sequence
from flask import Flask, jsonify, make_response, request
import jwt
import datetime
import os


import db.database


app = Flask(__name__)
SECRET_KEY = os.getenv('SECRET_KEY')

# engine = create_engine(os.getenv('MYSQL_DSN'))
# Base = declarative_base()
# Session = sessionmaker(bind=engine)
# session = Session()

# class User(Base):
# 	__tablename__ = 'users'

# 	id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
# 	name = Column(String(15))
# 	fullname = Column(String(15))
# 	password = Column(String(15))
# 	address = Column(String(15))

# 	def __repr__(self):
# 	    return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password, self.address)

# Base.metadata.create_all(engine)


@app.route('/')
def home():
    return jsonify({'url': [
        'login',
        'home'
    ]})


@app.route("/login")
def hello():
    token = {
        'public_id': 'Ardavan',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    token = jwt.encode(token, SECRET_KEY, algorithm='HS256')
    return jsonify(token=token.decode('UTF-8'))


@app.route("/env", methods=['POST', 'GET'])
def getinfo():
    new_user = User('Ardavan', 'Sassani', 'a.sassani@gmail.com', '12345')
    # new_user = User(name='ardook',password='12345',fullname='ardookkhan', address='anjasf435')
    # session.add(new_user)
    # our_user = session.query(User).filter_by(name='ardook').first()
    # session.commit()
    # User.session.add(new_user)
    return (new_user.fullname)
    # return os.getenv('SECRET_KEY')
    # return jsonify(dir(new_user))
