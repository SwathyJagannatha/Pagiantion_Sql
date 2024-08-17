from . import ma
from marshmallow import fields,validate

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    price =  fields.Float(required=True)
    qty = fields.Integer(required=True)
    class Meta:
        fields = ('id','name','price','qty')
        
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
