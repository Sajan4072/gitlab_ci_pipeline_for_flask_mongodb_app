from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
import urllib.parse
import os
from pathlib import Path

# print(Path(__file__))  # reference
# print(Path(__file__).resolve().parents[1]) # root

# The following code defines the absolute path of the .env file using the __init__.py location as a reference
# dotenv_path = str(Path(__file__).resolve().parents[1]) + "\.env"
# load_dotenv(dotenv_path)
load_dotenv()

username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")

app = Flask(__name__)
db_client = MongoClient(f"mongodb+srv://{urllib.parse.quote(username)}:{urllib.parse.quote(password)}@cluster0.dgdzi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
app_db = db_client["app"]  # replace "app" with the database name
product_collection = app_db["products"]  # replace "p

from app import routes
