from sqlalchemy import Column, String, text,ForeignKey
from sqlalchemy.dialects.mysql import INTEGER,FLOAT
from . import db

Base=db.Model
metadata=Base.metadata


class Shop(Base):
    __tablename__="shops"
    id=Column(INTEGER(20),primary_key=True)
    name=Column(String(30))
    description=Column(String(100))


    def as_dict(self):
        return {c.name: getattr(self,c.name) for c in self.__table__.columns}

class Item(Base):
    __tablename__="items"
    id=Column(INTEGER(20),primary_key=True)
    name=Column(String(30))
    description=Column(String(100))

    def as_dict(self):
        return {c.name: getattr(self,c.name) for c in self.__table__.columns} 
    
class Stocks(Base):
    __tablename__ ="stocks"
    id = Column(INTEGER(20),primary_key=True ) 
    item_id = Column(INTEGER(20),ForeignKey("items.id"))
    shop_id = Column(INTEGER(20),ForeignKey("shops.id"))
    unit_count=Column(INTEGER(20))
    unit_price=Column(FLOAT(20))

    def as_dict(self):
        return {c.name: getattr(self,c.name) for c in self.__table__.columns} 