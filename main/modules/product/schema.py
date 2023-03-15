from marshmallow import fields, pre_load, ValidationError

from main.extensions import ma
from main.modules.product.models import Product


# class BytesField(fields.Field):
#     def _validate(self, value):
#         if not isinstance(value, bytes):
#             raise ValidationError('Invalid input type.')

#         if value is None or value == b'':
#             raise ValidationError('Invalid value')


# class ImgSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = Img
#     image = fields.Str()
#     name = fields.Str()
#     mimetype = fields.Str()
# class ProductImageSchema(ma.SQLAlchemySchema):
#     class Meta:
#         model = ProductImage

#     image = fields.Str()


class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product

    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    date = fields.Date('%Y-%m-%d')
    category = fields.Str()
    price = fields.Int()
    quantity = fields.Int()
    Store = fields.Str()
    imgOb = fields.Str()
    img1 = fields.Str()
    img2 = fields.Str()
    # images = ma.Nested(ProductImageSchema, many=True)

    @pre_load
    def lower_product_ids(self, data, **kwargs):
        data['Store'] = 'OYAStore'
        print(data)
        return data
