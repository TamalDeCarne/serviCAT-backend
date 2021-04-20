from flask import Flask, escape, request, Blueprint, current_app, jsonify
#from json import loads as jloads
from api.models import City
from api.schemas import CitySchema
from flask_cors import CORS
from api.utils import helpers

city = Blueprint("city", __name__)
city_schema = CitySchema()
CORS(city)

@city.route("/api/cities", methods=["GET"])
def get_cities():
    try:
        return helpers.get_rows(City, city_schema)
    except Exception as e:
        return jsonify({"error": str(e)}), 500