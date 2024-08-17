from flask import request,jsonify
from models.schemas.productSchema import product_schema,products_schema
from services import productService
from marshmallow import ValidationError
from caching import cache
from utils.util import token_required,role_required
from datetime import date

@role_required
def save():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages),400
    
    product_save = productService.save(product_data)
    return product_schema.jsonify(product_save),201

@cache.cached(timeout=60)
def find_all():
    all_products = productService.find_all()
    return products_schema.jsonify(all_products),200

def find_all_paginate():
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))
    products =  productService.find_all_paginate(page,per_page)
    return products_schema.jsonify(products),200

def search_product():
    search_term = request.args.get("search")
    searched_item = productService.search_product(search_term)
    return products_schema.jsonify(searched_item)

def find_paginate_search():
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))
    search_term = request.args.get("search")
    products =  productService.find_paginate_search(search_term,page,per_page)
    return products_schema.jsonify(products),200

def get_top_selling_products():
    top_selling_products = productService.get_top_selling_products()
    result = [{"product_name": name, "total_quantity": quantity} for name, quantity in top_selling_products]

    return jsonify(result), 200

def get_production_efficiency():
    specific_date = request.args.get('specific_date', type=str,default=date.today())
    specific_date = date.fromisoformat(specific_date)
    production_efficiency = productService.get_production_efficiency(specific_date)
    return jsonify([
        {"product_name": name, "total_quantity_produced": total_quantity} 
        for name, total_quantity in production_efficiency
    ]), 200