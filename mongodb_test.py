from pymongo import MongoClient
import urllib.parse
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("mongodb_username")
password= os.getenv("mongodb_password")

#creating a client
db_client= MongoClient(f"mongodb+srv://{urllib.parse.quote(username)}:{urllib.parse.quote(password)}@cluster0.dgdzi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")



app_db = db_client["app"] #replace "app" with database name of database in production or staging
product_collection= app_db["products"] #replace "products" with the name of the collection in production or staging

product_list=[
    {
        "name":"Product 1",
        "tag":"new",
        "price":9.99
    },
{
        "name":"Product 1",
        "tag":"new",
        "price":9.99
    }

]
new_product={
        "name":"Product 3",
        "tag":"new",
        "price":9.99,
        "iamge":"url:/path/"
}

product_collection.insert_one(new_product)
