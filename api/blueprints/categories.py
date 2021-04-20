from flask import Flask, escape, request, Blueprint, current_app, jsonify
#from json import loads as jloads
from api.models import Category
from api.schemas import CategorySchema
from flask_cors import CORS
from api.utils import helpers

category = Blueprint("category", __name__)
category_schema = CategorySchema()
CORS(category)

@category.route("/api/categories", methods=["GET"])
def get_categories():
    try:
        return helpers.get_rows(Category, category_schema)
    except Exception as e:
        return jsonify({"error": str(e)}), 500