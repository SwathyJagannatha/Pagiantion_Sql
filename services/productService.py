from database import db
from models.product import Product
from models.order import Order
from models.orderProduct import order_product
from models.employeeProduct import employee_product
from sqlalchemy import select,func,desc

def save(product_data):
    new_product = Product(
        name = product_data['name'],price = product_data['price'])

    db.session.add(new_product)
    db.session.commit()
    db.session.refresh(new_product)
    return new_product

def find_all():
    query = select(Product)
    all_products = db.session.execute(query).scalars().all()
    return all_products

def find_all_paginate(page,per_page):
    products = db.paginate(select(Product),page=page,per_page=per_page)
    return products

def search_product(search_term):
    query = select(Product).where(Product.name.like(f'%{search_term}%'))
    search_products = db.session.execute(query).scalars().all()
    return search_products

#apply pagination to product search

def find_paginate_search(search_term,page,per_page):
    products = db.paginate(select(Product).where(Product.name.like(f'%{search_term}%')),page=page,per_page=per_page)
    return products

def get_top_selling_products():
    query = (
        db.session.query(
            Product.name,
            func.sum(order_product.c.quantity).label('total_quantity')
        )
        .join(order_product, Product.id == order_product.c.product_id)
        .group_by(Product.name)
        .order_by(desc('total_quantity'))
    )

    top_selling_products = db.session.execute(query).all()
    return top_selling_products

def get_production_efficiency(specific_date):
    query=(
        db.session.query(
            Product.name,
            func.sum(employee_product.c.quantity).label('Total_quantity')
        )
        .join(employee_product,Product.id == employee_product.c.product_id)
        .filter(employee_product.c.date == specific_date)
        .group_by(Product.name)   
    )

    production_efficiency = db.session.execute(query).all()
    return production_efficiency