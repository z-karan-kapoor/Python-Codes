from . import BaseRoute,ShopRoute, ItemRoute
from flask import Blueprint

def init_app(app):
    app.register_blueprint(BaseRoute.routes)
    app.register_blueprint(ShopRoute.routes)
    app.register_blueprint(ItemRoute.routes)
    return app
