from . import ma
from marshmallow import fields

class UserSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    username = fields.String(required=True)
    password =  fields.String(required=True)

    class Meta:
        fields = ('id','name','email','phone','username','password')
        
user_schema = UserSchema()
users_schema = UserSchema(many=True,exclude=["password"])
