from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db = create_engine('mysql://root:jesuisshui@localhost/renrenbook')
db.echo = True
class Users(Base):
    __tablename__ = 'users'
    
    uid = Column(Integer,primary_key=True)
    name = Column(String(40))
    tinyurl = Column(String(100))
    token = Column(String(100))
    join_time = Column(DateTime)
    last_time=Column(DateTime)
    def __init__(self,uid,name,tinyurl,join_time,last_time,token):
        self.uid=uid
        self.name=name
        self.join_time=join_time
        self.last_time=last_time
        self.tinyurl=tinyurl
        self.token=token
class Status():
    __tablename__ = 'status'
    
    def __init__(self):
        pass
    
class Emoticons(Base):
    __tablename__='emoticons'
    emotion = Column(String(40),primary_key=True)
    icon=Column(String(100))
    desc= Column(String(100))
    
    def __init__(self,emotion,icon,desc):
        self.emotion=emotion
        self.icon=icon
        self.desc=desc
    