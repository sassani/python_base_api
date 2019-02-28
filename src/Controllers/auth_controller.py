""" Authentication and Authorization module"""
from flask import request, g

from index import APP
# from base_controller import error
# from src.controllers.base_controller import error
# from src.controllers.responses.response import response
from src.controllers.responses import Error, response
from src.models.dtos import LoginUserDto
from src.models.user import User
from src.services.client_service import ClientService
from src.controllers.base_controller import authorized
from src.services.auth_service import AuthService
from src.helpers.enums import LoginUserType
from src.helpers.error_handlers import ErrorHandlers as EH


ERROR_CODE_A = '01'


@APP.route("/api/auth", methods=['POST'])
def auth():
    """ Authenticate user"""
    error_code_b = '00'
    login_user = LoginUserDto(request.json)

    # check client
    client = ClientService(login_user).client
    if not client.is_valid:
        error = Error(ERROR_CODE_A + error_code_b + '00',
                      'Unauthorized', 'Client is not valid')
        return response(401, error)

    auth_service = AuthService(login_user)
    if auth_service.authenticate():
        if not auth_service.authenticated_user.is_active:
            error = Error(ERROR_CODE_A + error_code_b + '01',
                          'suspended User', 'your account is suspended.')
            return response(401, error)

        auth_token = auth_service.token(client)
        return response(201, None, auth_token)
    else:
        description = 'Email or Password is not correct'
        if login_user.type is LoginUserType.REFRESH_TOKEN:
            description = 'Refresh token is not valid'
        error = Error(ERROR_CODE_A + error_code_b +
                      '02', 'Unauthorized', description)
        return response(401, error)

    error = Error(ERROR_CODE_A + error_code_b + '03',
                  'Unauthorized', 'Authentication has been failed')
    return response(401, error)


@APP.route("/api/auth", methods=['DELETE'])
@authorized
def logout():
    """ revoke user from login table"""
    error_code_b = '01'
    user: User = g.user
    auth_service = AuthService()
    try:
        auth_service.logout(user.current_login_id)
    except EH as err:
        return response(401, Error(ERROR_CODE_A + error_code_b + '00', err.title, err.detail))
    return response(204, message='User has logged out successfully')
