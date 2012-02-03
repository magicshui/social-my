from functools import wraps
from flask import g,request,render_template,redirect,url_for
'''
需要登录
'''
def login_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        if g.user is None:
            return redirect(url_for('login',next= request.url))
        return f(*args,**kwargs)
    return decorated_function
'''
description: 模板
'''
def templated(template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint \
                    .replace('.', '/') + '.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator