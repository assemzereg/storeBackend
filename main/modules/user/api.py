from flask import Blueprint
from flask.globals import request
from flask.json import jsonify
from main.modules.user.models import User
from main.shared.base_api import BaseAPI
from main.modules.user.schemas import UserSchema
from werkzeug.security import check_password_hash

from flask_jwt_extended import create_access_token

blueprint = Blueprint('user', __name__, url_prefix='/api')


@blueprint.route('/login', methods=['POST'])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(email=email).first()
    if not(user) or not(check_password_hash(user.password, password)):
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify({'access_token': access_token, 'user': UserSchema().dump(user)}), 200


class UserAPI(BaseAPI):
    route_base = 'users'

    model = User
    schema = UserSchema


UserAPI.register(blueprint)
