from webob.dec import wsgify
from paste import httpserver
from paste.proxy import TransparentProxy

class HTTPMiddleware(object):
    """
    serializes every request and response
    """

    def __init__(self, app):
        self._app = app

    @wsgify
    def __call__(self, req):
        result = req.get_response(self._app)
        return result

httpserver.serve(HTTPMiddleware(TransparentProxy()), "0.0.0.0", port=1024)
