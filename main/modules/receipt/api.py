from flask import Blueprint
from main.modules.receipt.models import Receipt
from main.shared.base_api import BaseAPI
from main.modules.receipt.schema import ReceiptSchema

blueprint = Blueprint('receipt', __name__, url_prefix='/api')


class ReceiptAPI(BaseAPI):
    route_base = 'receipts'

    model = Receipt
    schema = ReceiptSchema


ReceiptAPI.register(blueprint)
