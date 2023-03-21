from flask.views import MethodView
from ..models.All import db
from flask import request
from ..Common import get_shop, get_item_shop
import json
from ..services.Items import util_post


class Shops_Services(MethodView):
    def __init__(self):
        self.id = None

    def get(self, *args, **kwargs):              # Get Request from Shops table
        result = get_shop()
        if result is not None:
            result = {"success": True, "result": result, "code": 200}
            return result
        else:
            result = {"success": False,
                      "result": "INVALID RESULT", "code": 404}
            return result

    def post(self, *args, **kwargs):             # POST Request from Shops table
        try:
            params = json.loads(request.data)
            result = get_shop(params['id'])
            if result is not None:
                return util_post(result)
        except Exception as e:
            return {"Error": "Bad Request"}


class ItemsByShopServices(MethodView):
    def __init__(self):
        self.id = None

    def post(self, *args, **kwargs):                 # POST Request for Items from Shops table
        try:
            params = json.loads(request.data)
            result = get_item_shop(params['id'])
            return util_post(result)

        except Exception as e:
            return {"Error": "Bad Request"}
