""" Error respopnses"""
class ErrorHandlers(Exception):
    """ Error respopnses"""
    status_code = 400

    def __init__(self,
                 code,
                 title,
                 detail,
                 status_code=None,
                 payload=None
                ):
        Exception.__init__(self)
        self.code = code
        self.title = title
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """ a"""
        response_value = dict(self.payload or ())
        response_value['code'] = self.code
        response_value['title'] = self.title
        response_value['detail'] = self.detail
        return response_value
