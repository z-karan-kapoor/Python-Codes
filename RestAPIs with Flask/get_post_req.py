from flask import Flask, request

class requests_op:

    app = Flask(__name__)
    stores={}
    items={
            1:
                {
                        "name": "Chair",
                        "price": 15.99
                },
            2:
                {
                        "name": "Table",
                        "price": 17.99
                }
        }


    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.get("/store")
    def show_store():
        return {"stores":requests_op.items}

    @app.post("/store")
    def create_store():
        request_data=request.get_json()
        new_store={"name": request_data["name"],"items":[]}
        requests_op.stores.append(new_store)
        return new_store, 201

    @app.post("/store/<string:name>/item")
    def create_item(name):
        request_data=request.get_json()
        for store in requests_op.stores:
            if store["name"] == name:
                new_item={"name": request_data["name"],"price": request_data["price"]}
                store["items"].append(new_item)
                return new_item,201
        return {"message": "Store not found"},404

    @app.get("/store/<string:name>")
    def get_store(name):
        for store in requests_op.stores:
            if store["name"]==name:
                return store
        return {"meassge": "Store not found"}, 404

    @app.get("/store/<string:name>/item")
    def get_item_in_store(name):
        for store in requests_op.stores:
            if store["name"]==name:
                return {"items":store["items"]}
        return {"meassge": "Store not found"}, 404