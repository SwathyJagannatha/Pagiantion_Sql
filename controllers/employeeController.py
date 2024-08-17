from flask import request,jsonify
from models.schemas.employeeSchema import employee_schema,employees_schema
from services import employeeService
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        employee_data = employee_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages),400
    
    employee_saved = employeeService.save(employee_data)
    return employee_schema.jsonify(employee_data),201

@cache.cached(timeout=60)
def find_all():
    all_employees = employeeService.find_all()
    return employees_schema.jsonify(all_employees),200

def calculate_prod_total():
    all_employees = employeeService.calculate_prod_total()
    return employees_schema.jsonify(all_employees),200

def calculate_prod_total():
    try:
        # Call the service function to get totals
        totals = employeeService.calculate_prod_total()
        
        # Return the results as a JSON response with a status code of 200
        return jsonify(totals), 200
    except Exception as e:
        # Handle any exceptions that might occur during the process
        return jsonify({"error": str(e)}), 500