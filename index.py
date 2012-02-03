# -*- coding: utf-8 -*-
'''
Created on 2012-1-22

@author: AolneShui
'''
from functools import wraps
from flask import g,request,render_template,redirect,url_for
from User_Oauth import *
from CmdView import *
from AdminViews import *
app = Flask(__name__)
app.debug=True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# url views
user_oauth_login_view = LoginView.as_view("login_view")
user_oauth_url_view = OAuth.as_view('oauth_url')
cmd_view = CmdView.as_view('cmd_view')
admin_emoticons_view =EmoticonsAll.as_view('admin_emoticons_view')
# url rules
app.add_url_rule('/user/oauth',  view_func=user_oauth_url_view)
app.add_url_rule('/user/oauthlogin',  view_func=user_oauth_login_view)
app.add_url_rule('/cmd',view_func = cmd_view )
app.add_url_rule('/admin/emoticons',view_func=admin_emoticons_view)
if __name__=='__main__':
    app.run()
    