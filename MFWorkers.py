# -*- coding: utf-8 -*-
from MFConfig import *
from MFSql import *
import sqlalchemy
from sqlalchemy.exc import *
from MFUtils import *
class Workers():
    def get_friends(self,token,mid):
        _r=RRClient()
        response=_r.get_with_out_session(token,RR_FRIENDS_GETFRIENDS.copy())
        r=[]
        for x in response:
            f=Friends(x['id'],x['name'],x['tinyurl'],x['headurl'],mid)
            r.append(f)
        return r
    def save_friends(self,r):
         try:
           db_session.add_all(r)
           db_session.commit()
           return True
         except sqlalchemy.exc.IntegrityError:
           return False
    def get_status(self,uid,token):
        _r=RRClient()
        response=_r.get_with_out_session(token,RR_STATUS_GET.copy())
        r=[]
        for x in response:
            f=Status(x['status_id'],x['message'],x['time'],x['uid'])
            r.append(f)
        return r
    def save_status(self,r):
        try:
            db_session.add_all(r)
            db_session.commit()
            return True
        except sqlalchemy.exc.InvalidRequestError:
            print 'exist'
            return False
        
            
        