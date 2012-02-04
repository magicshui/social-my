from flask import *
from flask.views import *
from MFUtils import *
from MFConfig import *
from MFSql import *
class view_emoticons_get_all(MethodView):
    def get(self):
        _r = RRClient()
        response =  _r.get_with_session(RR_STATUS_GETEMOTICONS)
        
        for x in response:
            e=Emoticons(x["emotion"],x["icon"],x["desc"])
            db_session.add(e)
        #db_session.rollback()
        db_session.commit()
            
        return render_template('admin_emoticons_all.html',v=response)
class EmoticonsDelete(MethodView):
    def get(self):
        name=request.args.get['desc']
        db_session.delete()