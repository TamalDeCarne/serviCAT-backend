from flask import Flask, escape, request as requests, Blueprint, current_app, jsonify
from json import loads as jloads
from api.models import Request, RequestView
from api.schemas import RequestSchema, RequestViewSchema
from flask_cors import CORS
from api.utils import helpers

request = Blueprint("request", __name__)
request_schema = RequestSchema()
requestv_schema = RequestViewSchema()
CORS(request)

#Modify get request for select * from request view RequestView Model RequestViewSchema
@request.route("/api/requests", methods=["GET"])
def get_requests():
    try:
        return helpers.get_rows(Request, request_schema)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@request.route("/api/view-requests", methods=["GET"])
def view_requests():
    try:
        return helpers.get_rows(RequestView, requestv_schema)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@request.route("/api/request/<id>", methods=["GET"])
def get_request(id):
    try:
        examiner = helpers.Examiner(
            id=id,
            model=Request,
            schema=request_schema
        )
        return helpers.get_row(examiner)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@request.route("/api/request", methods=["POST"])
def create_request():
    try:
        new_request = jloads(requests.data)
        examiner = helpers.Examiner(
            model=Request,
            schema=request_schema,
            unwanted_columns=["id","date_requested"],
            json_data= new_request
        )
        return helpers.insert_row(examiner)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@request.route("/api/request/<id>", methods=["PUT"])
def update_request(id):
    try:
        examiner = helpers.Examiner(
            id=id,
            model=Request,
            schema=request_schema,
            unwanted_columns=["id","date_requested"],
            json_data=jloads(requests.data)
        )
        return helpers.update_row(examiner)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@request.route("/api/request/<id>", methods=["DELETE"])
def delete_request(id):
    try:
        examiner = helpers.Examiner(
            id=id,
            model=Request,
            schema=request_schema
        )
        return helpers.delete_row(examiner)
    except Exception as e:
        return jsonify({"error": str(e)}), 500