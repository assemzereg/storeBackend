import requests

from marshmallow import fields, pre_load, ValidationError

from main.extensions import ma
from main.modules.user.models import User

import re

from werkzeug.security import generate_password_hash

def validate_phoneNumber(value):
    if (not re.match(r'0[657][0-9]{8}', value)):
        raise ValidationError('not a valid phone number')

def validate_email(value):
    response = requests.get("https://isitarealemail.com/api/email/validate",params = {'email': value})
    status = response.json()['status']
    if status == "valid":
        pass
    elif status == "invalid":
        raise ValidationError('not a valid email')
    else :
        raise ValidationError('email was uknown')

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_only = ('password',)
        dump_only = ('id',)
    id = fields.Int()
    userName = fields.Str()
    email = fields.Email(validate=validate_email)
    phoneNumber = fields.Str(validate=validate_phoneNumber)
    Store = fields.Str()
    
    @pre_load
    def lower_user_ids(self, data, **kwargs):
        email = data.get('email', None)
        password = data.get('password', None)

        if email:
            data['email'] = email.lower()
        if password:
            data['password'] = generate_password_hash(password, method='sha256')
        data['Store'] = 'OYAStore'
        return data
