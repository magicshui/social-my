# -*- coding: utf-8 -*-
from MFConfig import *
from flask import *
from flask.views import *

import base64
import Cookie
import email.utils
import hashlib
import hmac
import logging
import os.path
import time
import urllib
from MFConfig import *
from Renren_Oauth import *
from MFSql import * 
from MFUtils import *
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
# get the login page of renren.
# generate the login oauth url
class view_login_renren(MethodView):
    def get(self):
        url = "%s?client_id=%s&redirect_uri=%s&response_type=%s" % (RENREN_AUTHORIZATION_URI,CLIENT_ID,REDIRECT_URI,RESPONSE_TYPE)
        return render_template("user_oauth.html",url=url)
# oauth success
# 1 get user info
# 2 get accesstoken 
# 3 generate the user into database
class view_oauthed_renren(MethodView):
    def get(self):
            
            verfication_code=request.args.get("code")
            args=dict(client_id=RENREN_APP_API_KEY)
            args["client_secret"] = RENREN_APP_SECRET_KEY
            args["code"] = verfication_code
            args["grant_type"] = "authorization_code"
            args["client_id"]=RENREN_APP_API_KEY
            args["redirect_uri"]=REDIRECT_URI
            response = urllib.urlopen(RENREN_ACCESS_TOKEN_URI + "?" + urllib.urlencode(args)).read()
            
            access_token = _parse_json(response)["access_token"]
            
            _r=RRClient()
            _p=Praser()
            _user_response= _r.get_with_out_session(access_token, RR_USERS_GETINFO.copy())
            
            u=_p.to_user( _user_response, access_token)
            x=db_session.add(u)
            db_session.commit()
            return render_template('user_oauthed.html',result=x)
# oauth failed
class view_oauth_failed_renren(MethodView):
    def get(self):
        pass
class view_logined_renren(MethodView):
    def get(self):
        pass

