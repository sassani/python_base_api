""" Error respopnses"""


class ErrorHandlers(Exception):
    """ Error respopnses"""

    def __init__(self,
                 title: str,
                 detail: str = None
                 ):
        Exception.__init__(self)
        self.title = title
        self.detail = detail
