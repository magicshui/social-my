from flask import *
from flask.views import MethodView
from sqlhelper import *
from Renren_Oauth import *
from urllib import *
from config import *
from MFUtils import *
class EmoticonsAll(MethodView):
    def get(self):
        
        response =  RRClient.get_with_session(RR_STATUS_GETEMOTICONS)
        
        return render_template('admin_emoticons_all.html',v=response)
        