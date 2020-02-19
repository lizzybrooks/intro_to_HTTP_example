#!/usr/bin/env python3
# File: factor.py
# ---------------
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

# Unfortunate code that needs to reside at the front of these scripts if we're
# to unify helpers functions to their own files without allowing them to be
# server endpoints.
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../lib")

from httputils import extractRequestParameter

import json
import math

def computeFactorization(n):
    """
    Computes the prime factorization of what's assumed to
    be a reasonably small positive number.  We require
    it be reasonably small so the algorithm returns fairly
    quickly.
    """
    factors = []
    factor = 2
    while n > 1:
        while n % factor == 0:
            factors.append(factor)
            n /= factor
        factor += 1
    return factors

def handleRequest():
    """
    Invoked to factor a reasonably small positive number
    and returns with a payload that includes its factorization.
    """
    number = extractRequestParameter("number")
    response = {}
    response["success"] = number.isdigit() and int(number) > 0 and int(number) <= 100000
    if response["success"]:
        response["number"] = int(number)
        response["factors"] = computeFactorization(int(number))
    
    responsePayload = json.dumps(response)
    print("Content-Length: " + str(len(responsePayload)))
    print("Content-Type: application/json")
    print()
    print(responsePayload)
        
handleRequest()