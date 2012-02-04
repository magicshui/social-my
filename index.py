# -*- coding: utf-8 -*-

from functools import wraps
from flask import g,request,render_template,redirect,url_for

from MFConfig import *
from MFUserView import *
from MFEmoticonViews import *

app = Flask(__name__)
app.debug=True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# views
login_renren_view = view_login_renren.as_view('login_renren_view')
oauthed_renren_view=view_oauthed_renren.as_view('oauthed_renren_view')
oauth_failed_renren_view =view_oauth_failed_renren.as_view('oauth_failed_view')
emoticons_get_all_view = view_emoticons_get_all.as_view('emoticon_get_all_view')
friends_get_all_view = view_user_friends_renren_all.as_view('user_friends_all')
user_status_renren_get_view =view_user_status_renren_get.as_view('user_status_get')
user_comments_renren_get_view=view_user_comments_renren_get.as_view('user_comments_get')
user_visitor_renren_get_view=view_user_visitor_renren_get.as_view('user_visitor_get')
ana_view=view_ana.as_view('ana_view')
# url views
app.add_url_rule('/login',view_func=login_renren_view)
app.add_url_rule('/user/oauthlogin',view_func=oauthed_renren_view)
app.add_url_rule('/oauth/fail',view_func=oauth_failed_renren_view)
app.add_url_rule('/emo/get',view_func=emoticons_get_all_view)
app.add_url_rule('/friends/get',view_func=friends_get_all_view)
app.add_url_rule('/user/status',view_func=user_status_renren_get_view)
app.add_url_rule('/user/comments',view_func=user_comments_renren_get_view)
app.add_url_rule('/user/v',view_func=user_visitor_renren_get_view)
app.add_url_rule('/user/ana',view_func=ana_view)
if __name__=='__main__':
    app.run()
    