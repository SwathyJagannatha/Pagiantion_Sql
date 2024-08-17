from flask import request,jsonify
from models.schemas.customerSchema import customer_schema,customers_schema
from services import customerService
from marshmallow import ValidationError
from caching import cache
from utils.util import token_required,role_required

@role_required
def save():
    try:
        customer_data = customer_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages),400
    
    customer_saved = customerService.save(customer_data)
    return customer_schema.jsonify(customer_data),201

@cache.cached(timeout=60)
def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers),200

def find_all_paginate():
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))
    customers =  customerService.find_all_paginate(page,per_page)
    return customers_schema.jsonify(customers),200

def find_total_orders():
    try:
        totals = customerService.find_total_orders()
        return jsonify(totals),200
    except Exception as e:
        return jsonify({'error':str(e)}),500

def get_customer_lifetime_value():
    threshold = request.args.get('threshold', default=1000, type=float)  # Example default threshold
    customer_lifetime_value = customerService.get_customer_lifetime_value(threshold)
    return jsonify([
        {"customer_name": name, "total_order_value": total_value} 
        for name, total_value in customer_lifetime_value
    ]), 200