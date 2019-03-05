"""Module"""
import os

from flask import jsonify

from index import APP

# from BaseController import BaseController



@APP.route('/api/')
def home():
    """<params>:"""
    return jsonify({'url': [
        'login',
        'home'
    ]})

@APP.route("/env", methods=['POST', 'GET'])
def getinfo():
    """<params>:"""
    # new_user = User('Ardavan', 'Sassani', 'a.sassani@gmail.com', '12345')
    # new_user = User(name='ardook',password='12345',fullname='ardookkhan', address='anjasf435')
    # session.add(new_user)
    # our_user = session.query(User).filter_by(name='ardook').first()
    # session.commit()
    # User.session.add(new_user)
    # return (new_user.fullname)
    return jsonify(dir(os))
    # return jsonify(dir(new_user))
