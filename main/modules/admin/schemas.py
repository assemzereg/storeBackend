import requests

from marshmallow import fields, pre_load, ValidationError

from main.extensions import ma
from main.modules.admin.models import Admin
import re


from werkzeug.security import generate_password_hash


def Validate_phoneNumber(value):
    if not re.match(r'0[657][0-9]{8}', value):
        raise ValidationError('not a phone number')


def validate_email(value):
    response = requests.get(
        "https://isitarealemail.com/api/email/validate", params={'email': value})
    status = response.json()['status']
    if status == "valid":
        pass
    elif status == "invalid":
        raise ValidationError('not a valid email')
    else:
        raise ValidationError('email was uknown')


class AdminSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Admin
        load_only = ('password',)
        dump_only = ('id',)
    id = fields.Int()
    adminName = fields.Str()
    email = fields.Str(validate=validate_email)
    phoneNumber = fields.Str(validate=Validate_phoneNumber)
    Store = fields.Str()

    @pre_load
    def lower_admin_ids(self, data, **kwargs):
        email = data.get('email', None)
        password = data.get('password', None)
        if email:
            data['email'] = email.lower()
        if password:
            data['password'] = generate_password_hash(
                password, method='sha256')
        return data
