#!/usr/bin/env python3
# File: prime-server.py
# ---------------------
# Used to bootstrap a server to listen to port 8000
# and enable a single service endpoint at scripts/factor.py,
# which assumed a single GET paramater called number
# and returns with an array of its prime factors.
# 
# http://localhost:8000/scripts/factor.py?number=96294000
#
# {
#    success: true,
#    number: 96294000,
#    factors: [2, 2, 2, 2, 3, 5, 5, 5, 11, 1459]
# }
#
# If the number param is missing, malformed, or out of range,
# then the respond will just be this:
#
# {
#    success: false
# }

from http.server import HTTPServer, CGIHTTPRequestHandler

DEFAULT_PORT = 8000
def runServer(port):
    CGIHTTPRequestHandler.cgi_directories = ['/scripts']
    server = HTTPServer(("", port), CGIHTTPRequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down server.")
        
runServer(DEFAULT_PORT)
