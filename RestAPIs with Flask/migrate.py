from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker,declarative_base
from src.models.All import Shop,Item,Stocks
from dotenv import load_dotenv
import os
import json

ROOT_DIR=os.path.join(os.path.dirname("__file__"),".")
DOT_ENV_PATH=os.path.join(ROOT_DIR,".env")
load_dotenv(DOT_ENV_PATH)

def getDBConnectionString():
    config={}
    config["username"]=os.getenv("DB_USERNAME")
    config["host"]=os.getenv("DB_HOST")
    config["password"]=os.getenv("DB_PASSWORD")
    config["database"]=os.getenv("DATABASE")
    config["port"]=os.getenv("DB_PORT")
    con_str= f"mysql+pymysql://{config['username']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
    return con_str

engine = create_engine(getDBConnectionString())
db_session=scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base=declarative_base()
Base.query=db_session.query_property()

if __name__=="__main__":
    Base.metadata.create_all(bind=engine)
    item=Item(id=6,name="Apple IPad",description="IPad 2")
    db_session.add(item)
    shop=Shop(id=6,name="IPad shop",description="Sells IPad")
    db_session.add(shop)
    stock=Stocks(id=2,item_id=item.id,shop_id=shop.id,unit_count=2,unit_price=4.8)
    db_session.add(stock)
    try:
        db_session.commit()
    except Exception as e:
        print(f"Error: Unable to commt DB. Please Try Again")