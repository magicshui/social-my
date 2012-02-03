# -*- coding: utf-8 -*-
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
from Renren_Oauth import *
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
class OAuth(MethodView):
    #: step 1 获取认证链接
    #  用户跳转
    def get(self):
        url = "%s?client_id=%s&redirect_uri=%s&response_type=%s" % (RENREN_AUTHORIZATION_URI,CLIENT_ID,REDIRECT_URI,RESPONSE_TYPE)
        return render_template("user_oauth.html",url=url)
class LoginView(MethodView):
    def get(self):
            verfication_code=request.args.get("code")
        # 第一次获取code
            if verfication_code:
                session["code"]=verfication_code
            
            args=dict(client_id=RENREN_APP_API_KEY)
            args["client_secret"] = RENREN_APP_SECRET_KEY
            args["code"] = session["code"]
            args["grant_type"] = "authorization_code"
            args["client_id"]=RENREN_APP_API_KEY
            args["redirect_uri"]=REDIRECT_URI
            response = urllib.urlopen(RENREN_ACCESS_TOKEN_URI + "?" + urllib.urlencode(args)).read()
            access_token = _parse_json(response)["access_token"]
            session['a_t']=access_token
            return render_template('user_oauthed.html')
class Friends(MethodView):
    def get(self):
            access_token= session['a_t']
            params = {"method": "friends.getFriends", "fields": "name,tinyurl",'page':'1','count':'3000'}
            api_client = RenRenAPIClient(access_token, RENREN_APP_API_KEY, RENREN_APP_SECRET_KEY)
            response2 = api_client.request(params);
            #x=str(response2).replace("u'", "'").replace('"', '').replace("'", '"')
            rx="{% raw %}"
            for x in response2:
                ma = x["tinyurl"]
                rx=rx+"<dl class='ob'><dt><a class='the_img'><img src='%s' class='m_sub_img'></a></dt></dl>" % ma
            rx+="{% endraw %}"
            return render_template("friends_get_status_all.html",xa=response2)
class UserView(MethodView):
    def get(self):
        pass

