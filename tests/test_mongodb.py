import os
import unittest
from app import app
from dotenv import load_dotenv
from pymongo import MongoClient
import urllib.parse

from app.routes import products


class TestMongoDB(unittest.TestCase):

    @classmethod
    def setUp(cls):
        load_dotenv("../.env")
        cls.app = app.test_client()
        cls.app.testing = True
        cls.username = os.environ["MONGODB_USERNAME"]
        cls.password = os.environ["MONGODB_PASSWORD"]
        cls.db_client = MongoClient(f"mongodb+srv://{urllib.parse.quote(cls.username)}:{urllib.parse.quote(cls.password)}@cluster0.dgdzi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        cls.db = cls.db_client["app"]
        cls.collection = cls.db["products"]

    @classmethod
    def tearDownClass(cls):
        cls.db_client.close()

    def test_connection(self):
        try:
            self.db_client.admin.command("ismaster")
            print("Connection to MongoDB is successful.")
        except ConnectionError:
            self.fail("Connection to MongoDB is not successful.")
    def test_fetch_data_products(self):
        product=self.collection.find_one({"name":"Product 1"})
        self.assertIsNotNone(product)
        self.collection.find_one({"tag": "new"})




if __name__ == "__main__":
    unittest.main()
