from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from models.schemas.userSchema import user_schema,users_schema
from services import userService #dont import the individual function, import the module as a whole
from marshmallow import ValidationError
from caching import cache
from utils.util import token_required,role_required

def login():
    try:
        credentials = request.json
        token = userService.login(credentials['username'], credentials['password'])
    except KeyError:
        return jsonify({'messages':'Invalid payload, expecting username and password'}), 401
    
    if token:
        return jsonify(token), 200
    else:
        return jsonify({'messages':'Invalid username or password'}), 401

@role_required
def save(): #name the controller will always be the same as the service function
    try:
        #try to validate the incoming data, and deserialize
        user_data = user_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    user_saved = userService.save(user_data)
    return user_schema.jsonify(user_data), 201


# @cache.cached(timeout=60)
# @admin_required

@token_required
def find_all():
    all_users = userService.find_all()
    return users_schema.jsonify(all_users),200

def find_all_paginate():
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))
    users = userService.find_all_paginate(page, per_page)
    return users_schema.jsonify(users), 200