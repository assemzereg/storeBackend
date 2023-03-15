from flask import Blueprint
from flask.globals import request
from flask.json import jsonify
from main.modules.admin.models import Admin
from main.shared.base_api import BaseAPI
from main.modules.admin.schemas import AdminSchema


from flask_jwt_extended import create_access_token

blueprint = Blueprint('admin', __name__, url_prefix="/api")


@blueprint.route('/login', prefix='/api')
class UserAPI(BaseAPI):
    route_base = 'admins'

    model = Admin
    schema = AdminSchema


UserAPI.register(blueprint)
