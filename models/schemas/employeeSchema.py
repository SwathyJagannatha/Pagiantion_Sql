from . import ma
from marshmallow import fields

class EmployeeSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)

    class Meta:
        fields = ('id','name','email','phone')
        
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)
