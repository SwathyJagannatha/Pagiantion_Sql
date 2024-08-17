from database import db
from sqlalchemy.orm import Session
from sqlalchemy import func, select
from models.employee import Employee
from models.customer import Customer
from models.product import Product
from models.employeeProduct import employee_product
from sqlalchemy import select
from sqlalchemy.sql import func

def save(employee_data):
    new_employee = Employee(
        name = employee_data['name'],email = employee_data['email'],phone=employee_data['phone'],
    )

    db.session.add(new_employee)
    db.session.commit()
    db.session.refresh(new_employee)
    return new_employee

def find_all():
    query = select(Employee)
    all_employees = db.session.execute(query).scalars().all()
    return all_employees

# Write a query to calculate the total quantity of products each employee has produced.
# Group the results by employee name.
# Use the Group By clause to group the data and the Sum function to calculate the total quantity.

def calculate_prod_total():
    session = Session()  # Ensure you have a session instance from your database setup
    
    # Construct the query using select and join properly
    query = select(
        Employee.name,
        func.count().label('total_products')  # Assuming there's no quantity and we're counting products
    ).select_from(
        Employee
    ).join(
        employee_product, Employee.id == employee_product.c.employee_id
    ).join(
        Product, Product.id == employee_product.c.product_id
    ).group_by(
        Employee.name
    )

    # Execute the query and fetch all results
    results = db.session.execute(query).fetchall()

    # Convert results into a list of dictionaries for easier JSON serialization
    return [{'name': employee_name, 'total_products': total_products} for employee_name, total_products in results]

