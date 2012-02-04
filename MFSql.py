# -*- coding: utf-8 -*-
from MFConfig import *
from datetime import *
import simplejson as json
db.echo = True
class Praser():
    def to_user(self,response,token):
        r=Users(response[0]["uid"],
                          response[0]['name'], 
                          response[0]['tinyurl'],
                          datetime.now(),
                        datetime.now(), token)
        return r
class Users(Base):
    __tablename__ = 'users'
    
    uid = Column(Integer,primary_key=True)
    name = Column(String(40))
    tinyurl = Column(String(100))
    token = Column(String(100))
    join_time = Column(DateTime)
    last_intime=Column(DateTime)
    def __init__(self,uid,name,tinyurl,join_time,last_time,token):
        self.uid=uid
        self.name=name
        self.join_time=join_time
        self.last_intime=last_time
        self.tinyurl=tinyurl
        self.token=token
class Status(Base):
    __tablename__ = 'status'
    
    status_id = Column(Integer,primary_key=True)
    comment_count = Column(Integer)
    message = Column(String(300))
    time = Column(DateTime)
    uid=Column(Integer)
    def __init__(self,status_id,comment_count,message,time,uid):
        self.status_id=status_id
        self.comment_count=comment_count
        self.message=message
        self.uid=uid
        self.time=time
class Comments(Base):
    
    __tablename__ = 'comments'
    
    uid = Column(Integer,primary_key=True)
    name =Column(String(40))
    tinyurl = Column(String(200))
    comment_id = Column(Integer)
    time = Column(DateTime)
    text = Column(String(500))
    def __init__(self,uid,name,tinyurl,comment_id,time,text):
        self.uid=uid
        self,name=name
        self.comment_id=comment_id
        self.time=time
        self.text=text
class Emoticons(Base):
    __tablename__='emoticons'
    emotion = Column(String(40),primary_key=True)
    icon=Column(String(100))
    desc= Column(String(100))
    
    def __init__(self,emotion,icon,desc):
        self.emotion=emotion
        self.icon=icon
        self.desc=desc

