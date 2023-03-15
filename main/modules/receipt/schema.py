from marshmallow import fields, pre_load, ValidationError

from main.extensions import ma
from main.modules.receipt.models import Receipt, Bought_Product


class Bought_ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Bought_Product
        dump_only = ('receipt_id')
    product_id = fields.Int()
    quantity = fields.Int()
    receipt_id = fields.Int()


class ReceiptSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Receipt

    id = fields.Int()
    user_id = fields.Int()
    total = fields.Int()
    bought_products = ma.Nested('Bought_ProductSchema', many=True)
