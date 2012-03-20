from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
import sys

class FlushLog( object ):
    def __init__( self ):
        if settings.DEBUG:
            pass
        else:
            raise MiddlewareNotUsed
    def process_response(self, request, response):
        #sys.stdout.write( repr(request) )
        sys.stdout.flush()
        sys.stderr.flush()
        return response
    def process_exception(self, request, exception):
        sys.stdout.flush()
        sys.stderr.flush()
