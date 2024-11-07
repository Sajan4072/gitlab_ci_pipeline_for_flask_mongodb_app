from app import app, product_collection
from flask import render_template




@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/products", methods=["GET"])  
def products():
    product_list = product_collection.find_one({"tag": "new"})
    return f"{product_list}"

