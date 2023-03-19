from flask.views import MethodView
from ..models.All import db
from flask import request
from ..Common import get_item,get_shop_item
import json

class Items_Services(MethodView):
    def __init__(self):
        self.id=None


    def get(self,*args, **kwargs):
        result=get_item()
        if result is not None:
            result={"success":True,"result":result,"code":200}
            return result
        else:
            result={"success":False,"result":"INVALID RESULT","code":404}
            return result

    def post(self,*args, **kwargs):
        params=json.loads(request.data)
        result=get_item(params['id'])
        if result is not None:
            result={"success":True,"result":result,"code":200}
            return result
        else:
            result={"success":False,"result":"INVALID RESULT","code":404}
            return result
        
class ShopByItemServices(MethodView):
    def __init__(self):
        self.id=None

    def post(self,*args, **kwargs):
        params=json.loads(request.data)
        result=get_shop_item(params['id'])
        if result is not None:
            result={"success":True,"result":result,"code":200}
            return result
        else:
            result={"success":False,"result":"INVALID RESULT","code":404}
            return result