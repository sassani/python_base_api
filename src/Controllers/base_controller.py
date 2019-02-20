""" Base controller for checking user autorization"""
from functools import wraps

from flask import jsonify, request

from index import APP
from src.Helpers.error_handlers import ErrorHandlers as eh


@APP.errorhandler(eh)
def handle_invalid_usage(error):
    """ Create Error messasge"""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def authorized(req):
    '''check token '''
    @wraps(req)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token is None:
            raise eh('000001', 'Forbiden',
                     'Authorization header is required', status_code=401)

        # check token and get users info
        # just do here everything what you need
        print('before home')
        result = req(*args, **kwargs)
        print('home result: %s' % result)
        # print(request.environ/['HTTP_AUTHORIZATION'])
        return result
    return wrapper


def convert_input_to(class_):
    '''Convert request to DTOs'''
    def wrap(f):
        def decorator(*args):
            obj = class_(**request.get_json())
            return f(obj)
        return decorator
    return wrap
