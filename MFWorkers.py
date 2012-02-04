# -*- coding: utf-8 -*-
from MFConfig import *
from MFSql import *
import sqlalchemy
from sqlalchemy.exc import *
from MFUtils import *
class Workers():
    def get_blogs(self,token,mid):
        _r=RRClient()
        params=RR_BLOG_GETS.copy()
        params['uid']=mid
        response=_r.get_with_out_session_with_dic(token, params,'blogs')
        r=[]
        for x in response:
            f=Blogs(x['uid'],
                    x['id'],
                    x['title'],
                    x['time'],
                    
                    x['view_count'],
                    x['comment_count'],
                    x['share_count'])
            r.append(f)
        return r
    def get_albums(self,token,mid):
        _r=RRClient()
        params=RR_PTHOTS_GETALBUMS.copy()
        params['uid']=mid
        response=_r.get_with_out_session(token, params)
        r=[]
        for x in response:
            f=Albums(x['uid'],
                     x['aid'],
                     x['name'],
                     x['description'],
                     x['size'],
                     x['comment_count'],
                     x['create_time']) 
            r.append(f)
        return r
    def _save(self,r):
        try:
           dbSession = sessionmaker(bind=db)
           db_session=dbSession()
           db_session.add_all(r)
           db_session.commit()
           return True
        except sqlalchemy.exc.IntegrityError:
           return False
    def _save_albums(self,r):
        self._save(r)
    
    def get_visitors(self,token,mid):
        _r =RRClient()
        r=_r.get_with_out_session_with_dic(token, RR_USERS_GETVISITORS.copy(),'visitors')
        return r
    def get_friends(self,token,mid):
        _r=RRClient()
        response=_r.get_with_out_session(token,RR_FRIENDS_GETFRIENDS.copy())
        r=[]
        for x in response:
            f=Friends(x['id'],x['name'],x['tinyurl'],x['headurl'],mid)
            r.append(f)
        return r
    def save_friends(self,r):
                self._save(r)

    def get_status(self,uid,token):
        _r=RRClient()
        response=_r.get_with_out_session(token,RR_STATUS_GET.copy())
        r=[]
        for x in response:
            f=Status(x['status_id'],x['message'],x['time'],x['uid'],x['comment_count'])
            r.append(f)
        return r
    def save_status(self,r):
                self._save(r)

    def _get_comment(self,token,uid,status_id):
        _r=RRClient()
        params=RR_STATUS_GETCOMMENT.copy()
        params['owner_id']=uid
        params['status_id']=status_id
        response=_r.get_with_out_session(token, params)
        r=[]
        for x in response:
            f=Comments(x['uid'],x['status_id'],x['name'],x['comment_id'],x['time'],x['text'])
            r.append(f)
        return r
    def _save_comments(self,r):
                self._save(r)

    def get_save_comments(self,token,uid,status_list):
        
        for x in status_list:
            r=self._get_comment(token,uid,x)
            self._save_comments(r)
        return True
            
            
        
            
        