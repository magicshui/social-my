from flask import Flask,render_template,session,request,redirect, url_for
from flask.views import MethodView
import base64
import Cookie
import email.utils
import hashlib
import hmac
import logging
import os.path
import time
import urllib
from config import *
# Find a JSON parser
try:
    import json
    _parse_json = lambda s: json.loads(s)
except ImportError:
    try:
        import simplejson
        _parse_json = lambda s: simplejson.loads(s)
    except ImportError:
        # For Google AppEngine
        from django.utils import simplejson
        _parse_json = lambda s: simplejson.loads(s)
class RenRenAPIClient(object):
    def __init__(self, access_token = None, api_key = None, secret_key = None):
        self.access_token = access_token
        self.api_key = api_key
        self.secret_key = secret_key
    def request(self, params = None):
        """Fetches the given method's response returning from RenRen API.

        Send a POST request to the given method with the given params.
        """
        params["api_key"] = self.api_key
        params["call_id"] = str(int(time.time() * 1000))
        params["format"] = "json"
        params["access_token"] = self.access_token
        params["v"] = '1.0'
        sig = self.hash_params(params);
        params["sig"] = sig
        
        post_data = None if params is None else urllib.urlencode(params)
        
        #logging.info("request params are: " + str(post_data))
        
        file = urllib.urlopen(RENREN_API_SERVER, post_data)
        
        try:
            s = file.read()
            logging.info("api response is: " + s)
            response = _parse_json(s)
        finally:
            file.close()
        if type(response) is not list and response["error_code"]:
            logging.info(response["error_msg"])
            raise RenRenAPIError(response["error_code"], response["error_msg"])
        return response
    def hash_params(self, params = None):
        hasher = hashlib.md5("".join(["%s=%s" % (self.unicode_encode(x), self.unicode_encode(params[x])) for x in sorted(params.keys())]))
        hasher.update(self.secret_key)
        return hasher.hexdigest()
    def unicode_encode(self, str):
        """
        Detect if a string is unicode and encode as utf-8 if necessary
        """
        return isinstance(str, unicode) and str.encode('utf-8') or str
    
class RenRenAPIError(Exception):
    def __init__(self, code, message):
        Exception.__init__(self, message)
        self.code = code


