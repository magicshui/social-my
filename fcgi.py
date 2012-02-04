#-*- encoding: utf-8 -*-
from index import app
from flup.server.fcgi import WSGIServer    
WSGIServer(app,bindAddress='/tmp/myapp.sock').run()