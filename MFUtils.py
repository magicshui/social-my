# -*- coding: utf-8 -*-
from MFConfig import *
from Renren_Oauth import *
from flask import *
from MFUserView import *
class RRClient():
    def __init__(self):
        pass
    def get_with_out_session(self,token,params):
        api_client = RenRenAPIClient(token, RENREN_APP_API_KEY, RENREN_APP_SECRET_KEY)
        response = api_client.request(params)
        return response
    def get_with_session(self,params):
        return self.get_with_out_session(session['t'], params)
    def get_with_out_session_with_dic(self,token,params,f):
        api_client = RenRenAPIClient(token, RENREN_APP_API_KEY, RENREN_APP_SECRET_KEY)
        response = api_client.request_dict(params, f)
        return response
class APPClient():
    def __init__(self):
        pass
    def add(self,view_class,url):
        exec('import index')
        exec('from index import *')
        exec('%s_view=%s.as_view("%s__view")' % (view_class.__name__,view_class.__name__,view_class.__name__))
        exec("index.app.add_url_rule('%s',view_func=%s_view)" % (url,view_class.__name__))
        return app