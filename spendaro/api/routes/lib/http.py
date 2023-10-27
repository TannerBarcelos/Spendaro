from enum import Enum

'''
Enum for HTTP methods (GET, POST, PUT, DELETE), HTTP status codes (200, 201, 202, 204, 400, 401, 403, 404, 500), and HTTP headers (Content-Type, etc.)
'''

class HTTPMethods(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'

class HTTPStatusCodes(Enum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

class HTTPHeaders(Enum):
    CONTENT_TYPE = 'Content-Type'
    