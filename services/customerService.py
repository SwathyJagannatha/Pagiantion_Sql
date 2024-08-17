from database import db
from models.customer import Customer
from models.order import Order
from models.product import Product
from models.orderProduct import order_product
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import func, select

def save(customer_data):
    new_customer = Customer(
        name = customer_data['name'],email = customer_data['email'],phone=customer_data['phone'],
        username = customer_data['username'],password = customer_data['password']
    )

    db.session.add(new_customer)
    db.session.commit()
    db.session.refresh(new_customer)
    return new_customer

def find_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers

def find_all_paginate(page,per_page):
    customers = db.paginate(select(Customer),page=page,per_page=per_page)
    return customers

# Task 3: Determine Customer Lifetime Value

# Write a query to calculate the total value of orders placed by each customer.
# Group the results by customer name.
# Use the Group By clause to group the data and the Sum function to calculate the total order value.
# Filter out customers with a total order value less than a certain threshold using the Having clause.

def find_total_orders():
    session = Session 
    # query = select(Customer).join(Order).where(Customer.id == Order.customer_id).filter(Customer.email == email)
    # orders = db.session.execute(query).scalars().all()
    # return orders
    threshold = 10.00
    query = select(
        Customer.name,
        func.sum(Product.price).label('total_order_value')  # Sums up product prices directly, not accounting for quantities ordered
    ).select_from(
        Customer
    ).join(
        Order, Customer.id == Order.customer_id
    ).join(
        order_product, Order.id == order_product.c.order_id
    ).join(
        Product, Product.id == order_product.c.product_id
    ).group_by(
        Customer.name
    ).having(
        func.sum(Product.price) >= threshold
    )

    results = session.execute(query).fetchall()

    return [{'customer_name': name, 'total_order_value': value} for name, value in results]


def get_customer_lifetime_value(threshold):
    query = (
        db.session.query(
            Customer.name,
            func.sum(Product.price * order_product.c.quantity).label('total_order_value')
        )
        .join(Order, Customer.id == Order.customer_id)
        .join(order_product, Order.id == order_product.c.order_id)
        .join(Product, Product.id == order_product.c.product_id)
        .group_by(Customer.name)
        .having(func.sum(Product.price * order_product.c.quantity) >= threshold)
        .order_by(func.sum(Product.price * order_product.c.quantity).desc())
    )

    customer_lifetime_value = db.session.execute(query).all()
    return customer_lifetime_value