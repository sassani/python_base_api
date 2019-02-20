""" Authentication and Authorization module"""
from flask import jsonify, request, make_response

from index import APP
# from src.Controllers.base_controller import authorized
# from src.Controllers.base_controller import convert_input_to
from src.services.auth_service import AuthService
from src.models.dtos import LoginUserDto


@APP.route("/api/auth", methods=['POST'])
# @convert_input_to(LoginUserDto)
def auth():
    """ Authenticate user"""
    login_user = LoginUserDto(request.json)
    auth_service = AuthService(login_user)
    if(auth_service.authenticate()):
        # get token

        return jsonify(token='token')
    else:
        return make_response('error response', 500)
