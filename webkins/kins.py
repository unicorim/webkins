from webob.dec import wsgify
from paste import httpserver
from paste.proxy import TransparentProxy


def print_trip(request, response):
    """
    just prints the request and response
    """
    print "Request\n==========\n\n"
    print str(request)
    print "\n\n"
    print "Response\n==========\n\n"
    print str(response)
    print "\n\n"


class HTTPMiddleware(object):
    """
    serializes every request and response
    """

    def __init__(self, app, record_func=print_trip):
        self._app = app
        self._record = record_func

    @wsgify
    def __call__(self, req):
        result = req.get_response(self._app)
        try:
            self._record(req.copy(), result.copy())
        except Exception, ex: #return response at all costs
            print ex
        return result

httpserver.serve(HTTPMiddleware(TransparentProxy()), "0.0.0.0", port=1024)
