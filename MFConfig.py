# -*- coding: utf-8 -*-
'''
Created on 2012-1-23

@author: AolneShui
'''
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

RENREN_APP_API_KEY = "e7427195f99e4043bb34c2b8a7c40b65"
RENREN_APP_SECRET_KEY = "e8e30383e1c64f92bbfd144c2f2250fa"
RENREN_AUTHORIZATION_URI = "http://graph.renren.com/oauth/authorize"
RENREN_ACCESS_TOKEN_URI = "http://graph.renren.com/oauth/token"
RENREN_SESSION_KEY_URI = "http://graph.renren.com/renren_api/session_key"
RENREN_API_SERVER = "http://api.renren.com/restserver.do"
REDIRECT_URI = "http://127.0.0.1:5000/user/oauthlogin"
APP_KEY = "e7427195f99e4043bb34c2b8a7c40b65"
APP_SECRET = "e8e30383e1c64f92bbfd144c2f2250fa"
CLIENT_ID = "e7427195f99e4043bb34c2b8a7c40b65"
RESPONSE_TYPE = 'code' #固定值，请勿修改
CODE = "code"
# database 
DATABASE_USER = 'root'
DATABASE_PWD = 'jesuisshui'
DATABASE_NAME= 'renrenbook'
# renren apis
RR_STATUS_GETEMOTICONS = {"method": "status.getEmoticons", "format": "json",'type':'all'}
RR_USERS_GETINFO={"method":"users.getInfo","format":"json"}
RR_FRIENDS_GETFRIENDS= {"method": "friends.getFriends", "fields": "name,tinyurl",'page':'1','count':'3000'}


db = create_engine('mysql://%s:%s@localhost/%s'% (DATABASE_USER,DATABASE_PWD,DATABASE_NAME),connect_args={'charset':'utf8'},echo=True )
Session = sessionmaker(bind=db)
db_session=Session()