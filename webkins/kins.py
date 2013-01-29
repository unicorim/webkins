from webob.dec import wsgify
from paste import httpserver
from paste.proxy import TransparentProxy
import urlparse

def yrk(appkin):
    url = urlparse.urlparse(appkin)
    string, path = url.netloc, url.path
    if path == "/*":
        block = string
    else:
        block = "http://" +  string + path
    return block


class HTTPMiddleware(object):
    def __init__(self, app, kin, layer):
        self._app = app
        self.appkin = kin
        self.layer = layer

    @wsgify
    def __call__(self, req):
        url, irl = yrk(self.appkin), urlparse.urlsplit(req.url)
        if url in irl.geturl():
            return self.layer
        else:
            return self._app
