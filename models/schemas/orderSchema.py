from . import ma
from marshmallow import fields,validate

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    date = fields.Date(required=True)
    customer_id =  fields.Integer(required=True)

    class Meta:
        fields = ('id','date','customer_id')
        
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
