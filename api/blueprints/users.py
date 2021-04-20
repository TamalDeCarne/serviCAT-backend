from flask import Flask, escape, request, Blueprint, current_app, jsonify
from json import loads as jloads
from api.models import User
from api.schemas import UserSchema
from flask_cors import CORS
from api.utils import helpers
from api import bycrypt

user = Blueprint("user", __name__)
user_schema = UserSchema()
CORS(user)

#Modify get request for select * from request view RequestView Model RequestViewSchema
@user.route("/api/users", methods=["GET"])
def get_users():
    try:
        return helpers.get_rows(User, user_schema)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user.route("/api/user/<id>", methods=["GET"])
def get_user(id):
    try:
        examiner = helpers.Examiner(
            id=id,
            model=user,
            schema=user_schema
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user.route("/api/user", methods=["POST"])
#add bcrypt encryption
def create_user():
    try:
        examiner = helpers.Examiner(
            model=User,
            schema=user_schema,
            unwanted_columns=["id"],
            json_data=jloads(request.data)
        )
        return helpers.insert_row(examiner)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user.route("/api/user", methods=["PUT"])
#add bycrypt encryption
def update_user():
    try:
        examiner = helpers.Examiner(
            model=user,
            schema=user_schema,
            unwanted_columns=["id","date_requested"],
            json_data=jloads(request.data)
        )
        return helpers.update_row(examiner)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user.route("/api/user", methods=["DELETE"])
def delete_user():
    try:
        examiner = helpers.Examiner(
            id=id,
            model=user,
            schema=user_schema
        )
        return helpers.delete_row(examiner)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user.route("/api/login", methods=["POST"])
def log_in():
    try:
        login_credentials = jloads(request.data)
        usuario = User.query.filter_by(email=login_credentials["email"]).first()

#        if (usuario is not None) and bycrypt.check_password_hash(usuario.password, login_credentials["password"]):
        if (usuario is not None) and (usuario.password == login_credentials["password"]):
            return jsonify({"validCredentials": True, "user_id": usuario.id}), 200
        else:
            return jsonify({"validCredentials": False}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500