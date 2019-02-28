""" manage all responses to client"""
import jsons
from flask import make_response


class Error:
    """ Error object model"""
    def __init__(self,
                 code,
                 title,
                 detail):
        """create and return error response"""
        self.code = code
        self.title = title
        self.detail = detail


def response(
        status: int = 400,
        error: Error = None,
        data: object = None,
        meta: object = None,
        links: object = None,
        message: str = None
):
    """Create and return generic response"""
    payload = {}
    if error is not None:
        payload = {
            'error': error
        }
    elif data is not None:
        payload = {
            'data': data,
            'meta': meta,
            'links': links
        }
    else:
        payload = {
            'message': message
        }
    res = make_response(jsons.dumps(payload), status)
    res.headers['Content-Type'] = 'application/json; charset=utf-8'
    return res
