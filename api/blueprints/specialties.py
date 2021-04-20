from flask import Flask, escape, request, Blueprint, current_app, jsonify
#from json import loads as jloads
from api.models import Specialty
from api.schemas import SpecialtySchema
from flask_cors import CORS
from api.utils import helpers

specialty = Blueprint("specialty", __name__)
specialty_schema = SpecialtySchema()
CORS(specialty)

@specialty.route("/api/specialties", methods=["GET"])
def get_specialties():
    try:
        return helpers.get_rows(Specialty, specialty_schema)
    except Exception as e:
        return jsonify({"error": str(e)}), 500