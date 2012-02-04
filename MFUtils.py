# -*- coding: utf-8 -*-
from MFConfig import *
from Renren_Oauth import *
from flask import *
class RRClient():
    def __init__(self):
        pass
    def get_with_out_session(self,token,params):
        api_client = RenRenAPIClient(token, RENREN_APP_API_KEY, RENREN_APP_SECRET_KEY)
        response = api_client.request(params)
        return response
    def get_with_session(self,params):
        return self.get_with_out_session(session['t'], params)