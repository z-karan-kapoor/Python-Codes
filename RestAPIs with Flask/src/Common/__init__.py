from ..models.All import Shop,Item,Stocks

def get_values(idx,id):
    if id == None:
        result=[s.as_dict() for s in idx.query.all()]
        return result
    return [s.as_dict() for s in idx.query.filter(id==idx.id)]

def get_shopID_values(idx,id):
    if id == None:
        result=[s.as_dict() for s in idx.query.all()]
        return result
    return [s.as_dict() for s in idx.query.filter(id==idx.shop_id)]

def get_itemID_values(idx,id):
    if id == None:
        result=[s.as_dict() for s in idx.query.all()]
        return result
    return [s.as_dict() for s in idx.query.filter(id==idx.item_id)]

def get_shop(id=None):
    return get_values(Shop,id)
        
def get_item(id=None):
    return get_values(Item,id)

def get_shop_item(shop_id=None):
    return get_shopID_values(Stocks,shop_id)

def get_item_shop(item_id=None):
    return get_itemID_values(Stocks,item_id)