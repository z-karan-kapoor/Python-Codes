from .BaseRoute import get_New_Route
from ..services.Shops import Shops_Services,ItemsByShopServices

routes=get_New_Route('shops')
routes.add_url_rule('/',view_func=Shops_Services.as_view('shops'),methods=['GET','POST'])

routes.add_url_rule('/items',view_func=ItemsByShopServices.as_view('stocks'),methods=['POST'])