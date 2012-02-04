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
                         token)
        return r
    def to_friends(self,response,token):
        pass
class Blogs(Base):
    __tablename__='blogs'
    uid=Column(BigInteger)
    id=Column(BigInteger,primary_key=True)
    btime=Column(DateTime)
    title=Column(String(100))
    view_count=Column(Integer)
    comment_count=Column(Integer)
    share_count=Column(Integer)
    def __init__(self,uid,id,title,time,view_count,comment_count,share_count):
        self.uid=uid
        self.id=id
        self.btime=time
        self.title=title
        self.view_count=view_count
        self.comment_count=comment_count
        self.share_count=share_count
class Albums(Base):
    __tablename__='albums'
    uid=Column(BigInteger)
    aid=Column(BigInteger,primary_key=True)
    name=Column(String(200))
    description=Column(String(400))
    size=Column(Integer)
    ctime=Column(DateTime)
    comment_count=Column(Integer)
    def __init__(self,uid,aid,name,description,size,comment_count,time):
        self.aid=aid
        self.comment_count=comment_count
        self.ctime=time
        self.description=description
        self.name=name
        self.size=size
        self.uid=uid
class Friends(Base):
    __tablename__='friends'
    uid = Column(BigInteger,primary_key=True)
    name=Column(String(40))
    tinyurl=Column(String(100))
    headurl=Column(String(200))
    mid=Column(BigInteger)
    def __init__(self,uid,name,tinyurl,headurl,mid):
        self.uid=uid
        self.name=name
        self.headurl=headurl
        self.tinyurl=tinyurl
        self.mid=mid

class Users(Base):
    __tablename__ = 'users'
    
    uid = Column(BigInteger,primary_key=True)
    name = Column(String(40))
    tinyurl = Column(String(100))
    token = Column(String(100))
    join_time = Column(DateTime)
    
    def __init__(self,uid,name,tinyurl,join_time,token):
        self.uid=uid
        self.name=name
        self.join_time=join_time
      
        self.tinyurl=tinyurl
        self.token=token
class Status(Base):
    __tablename__ = 'status'
    
    comment_count =Column(Integer)
    status_id = Column(BigInteger,primary_key=True)
    message = Column(String(300))
    stime = Column(DateTime)
    uid=Column(BigInteger)
    def __init__(self,status_id,message,time,uid,comment_count):
        self.status_id=status_id
        self.message=message
        self.uid=uid
        self.comment_count=comment_count
        self.stime=time
class Comments(Base):
    
    __tablename__ = 'comments'
    status_id =Column(BigInteger)
    uid = Column(BigInteger,primary_key=True)
    name =Column(String(40))
    comment_id = Column(Integer)
    ctime = Column(DateTime)
    text = Column(String(500))
    def __init__(self,uid,status_id,name,comment_id,time,text):
        self.uid=uid
        self.status_id=status_id
        self.name=name
        self.comment_id=comment_id
        self.ctime=time
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

