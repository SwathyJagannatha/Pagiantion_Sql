from flask import Blueprint 
from controllers.customerController import save,find_all,find_all_paginate,get_customer_lifetime_value

customer_blueprint = Blueprint('customer_bp',__name__)

customer_blueprint.route('/',methods=['POST'])(save)
customer_blueprint.route('/',methods=['GET'])(find_all)

customer_blueprint.route('/paginate',methods=['GET'])(find_all_paginate)

customer_blueprint.route('/lifetime_value',methods=['GET'])(get_customer_lifetime_value)

