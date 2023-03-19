from .BaseRoute import get_New_Route
from ..services.Items import Items_Services,ShopByItemServices

routes=get_New_Route('items')
routes.add_url_rule('/',view_func=Items_Services.as_view('items'),methods=['GET','POST'])

routes.add_url_rule('/shops',view_func=ShopByItemServices.as_view('stocks'),methods=['POST'])