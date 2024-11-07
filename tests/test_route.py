from app import app
import unittest
import os
from dotenv import load_dotenv

class RouteTest(unittest.TestCase):
    def setUp(self):
        load_dotenv("../.env")
        self.app = app.test_client()
        self.app.testing =True

    def test_index_get(self):
        # mock sending a request to the index page
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_index_post(self):
        # mock sending a request to the index page
        response = self.app.post("/")
        self.assertEqual(response.status_code, 405)

    def test_products(self):
        response = self.app.get("/products")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
