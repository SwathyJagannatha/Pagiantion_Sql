from flask import Blueprint 
from controllers.productController import save,find_all,find_all_paginate,search_product,find_paginate_search,get_top_selling_products,get_production_efficiency

product_blueprint = Blueprint('product_bp',__name__)

product_blueprint.route('/',methods=['POST'])(save)
product_blueprint.route('/',methods=['GET'])(find_all)

product_blueprint.route('/paginate',methods=['GET'])(find_all_paginate)

product_blueprint.route('/search',methods=['GET'])(search_product)

product_blueprint.route('/paginate_search',methods=['GET'])(find_paginate_search)

product_blueprint.route('/top_selling', methods=['GET'])(get_top_selling_products)

product_blueprint.route('/production_efficiency', methods=['GET'])(get_production_efficiency)