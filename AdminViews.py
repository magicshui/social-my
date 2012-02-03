from flask import *
from flask.views import MethodView
from sqlhelper import *
from Renren_Oauth import *
from urllib import *
from config import *
class EmoticonsAll(MethodView):
    def get(self):
        access_token=session['a_t']
        params = {"method": "status.getEmoticons", "format": "json",'type':'all'}
        api_client = RenRenAPIClient(access_token, RENREN_APP_API_KEY, RENREN_APP_SECRET_KEY)
        response = api_client.request(params)
        
        return render_template('admin_emoticons_all.html',v=response)
        