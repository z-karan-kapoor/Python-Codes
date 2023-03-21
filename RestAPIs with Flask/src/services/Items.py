from flask.views import MethodView
from ..models.All import db
from flask import request
from ..Common import get_item,get_shop_item
import json

@staticmethod
def util_post(result):
    """This is to return success/failure on Post request"""
    if result is not None:
        result = {"success": True, "result": result, "code": 200}
        return result
    else:
        result = {"success": False,
        "result": "INVALID RESULT", "code": 404}
        return result

class Items_Services(MethodView):
    def __init__(self):
        self.id=None


    def get(self,*args, **kwargs):              # Get Request from Items table
        result=get_item()
        if result is not None:
            result={"success":True,"result":result,"code":200}
            return result
        else:
            result={"success":False,"result":"INVALID RESULT","code":404}
            return result

    def post(self,*args, **kwargs):         # POST Request from Items table
        try:
            params=json.loads(request.data)
            result=get_item(params['id'])
            return util_post(result)
        except Exception as e:
            return {"Error": "Bad Request"}
        
class ShopByItemServices(MethodView):
    def __init__(self):
        self.id=None

    def post(self,*args, **kwargs):             # POST Request for Shops from Items table
        try:
            params=json.loads(request.data)
            result=get_shop_item(params['id'])
            return util_post(result)
        except Exception as e:
            return {"Error": "Bad Request"}