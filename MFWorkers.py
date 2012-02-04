# -*- coding: utf-8 -*-
from MFConfig import *
from MFSql import *
from MFUtils import *
class Workers():
    def get_friends(self,token):
        _r=RRClient()
        response=_r.get_with_out_session(token,RR_FRIENDS_GETFRIENDS.copy())
        r=[]
        for x in response:
            f=Friends(x['id'],x['name'],x['tinyurl'],x['headurl'])
            r.append(f)
        return r