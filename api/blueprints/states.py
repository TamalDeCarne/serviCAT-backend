from flask import Flask, escape, request, Blueprint, current_app, jsonify
from json import loads as jloads
from api.models import State
from api.schemas import StateSchema
from flask_cors import CORS
from api.utils import helpers

state = Blueprint("state", __name__)
state_schema = StateSchema()
CORS(state)

@state.route("/api/states", methods=["GET"])
def get_states():
    try:
        return helpers.get_rows(State, state_schema)
    except Exception as e:
        return jsonify({"error": str(e)}), 500