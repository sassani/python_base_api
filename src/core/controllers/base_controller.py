""" Base controller for checking user autorization"""
from functools import wraps

from flask import g, request

from src.core.controllers.responses import Error, response
from src.core.services.auth_service import AuthService
from src.core.helpers.error_handlers import ErrorHandlers as EH

ERROR_CODE_A = '00'


def authorized(req):
    '''check token '''
    error_code_b = '00'
    @wraps(req)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token is None:
            return response(401, Error(ERROR_CODE_A + error_code_b + '00', 'Forbiden', 'Authorization header is required'))
        auth_service = AuthService()
        try:
            auth_service.authorize(token)
            g.user = auth_service.authenticated_user
        except EH as err:
            return response(401, Error(ERROR_CODE_A + error_code_b + '01', err.title, err.detail))

        return req(*args, **kwargs)
    return wrapper
