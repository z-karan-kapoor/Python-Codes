from flask import Blueprint

def get_New_Route(name):
    return Blueprint(name,__name__,url_prefix='/' + name)

def check():
    return "<h1>Welcome to the Flask App Base!</h1>"

routes=Blueprint("base",__name__,url_prefix='/')
routes.add_url_rule('/',view_func=check)
