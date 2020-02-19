# File: httputlis.py
# ------------------
# Defines a small set of Python convenience functions to
# extract isolated parameters from query strings and to
# pull out the payload and payload type of POST requests.

import cgi, os, sys

def extractRequestParameter(param):
    """
    Returns the value attached to the key within the query string
    of the request URL.  If, for instance, the query string is
    a=123&b=hello, then extractRequestParam("a") would return "123",
    extractRequestParam("b") would return "hello", and extractRequestParam("c")
    would return None
    """
    params = cgi.FieldStorage()
    if param not in params: return None
    return params[param].value

def extractContentType():
    """
    Returns the content type of a POST request's payload, or
    None of the request isn't a POST
    """
    if os.environ["REQUEST_METHOD"] != "POST": return None
    return os.environ["CONTENT_LENGTH"]

def extractPayload():
    """
    Returns the payload of a POST request, or the "" if
    the request isn't actually a POST
    """    
    if os.environ["REQUEST_METHOD"] != "POST": return ""
    length = int(os.environ["CONTENT_LENGTH"])
    payload = sys.stdin.read(length)
    return payload
