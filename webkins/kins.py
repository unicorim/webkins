from webob.dec import wsgify
from paste import httpserver
from paste.proxy import TransparentProxy
import urlparse

class HTTPMiddleware(object):
    def __init__(self, app):
        self._app = app

    @wsgify
    def __call__(self, req):
        url_bits = urlparse.urlsplit(req.url)
        if "facebook.com" in url_bits.netloc:
            return "<html><head><title>Hello</title></head><body>yo</body></html>"
        else:
            return req.get_response(self._app)

httpserver.serve(HTTPMiddleware(TransparentProxy()), "0.0.0.0", port=1024)
