Factory Management System
..........................
This repository contains the backend implementation of a Factory Management System using Flask. The system includes functionalities for managing customers, products, orders, and employees. The implementation also includes advanced querying and pagination features for efficient data retrieval.

Project Structure

app.py: The main application file where the Flask app is configured, including the registration of blueprints.
blueprints: This folder contains all the blueprint configurations for different modules like customers, products, orders, and employees.
controllers: This folder contains the controller files for handling API requests for each module.
services: This folder contains the service files that include business logic for processing data.
models: This folder contains the SQLAlchemy models representing the database schema.
database.py: This file handles the database connection and session management.

API Endpoints

Customer Management
Blueprint: customer_blueprint
URL Prefix: /customers

POST /customers/: Save a new customer.
GET /customers/: Retrieve all customers.
GET /customers/paginate: Retrieve customers with pagination.
GET /customers/lifetime_value: Calculate and retrieve the lifetime value of each customer.

Product Management

Blueprint: product_blueprint

URL Prefix: /products

POST /products/: Save a new product.
GET /products/: Retrieve all products.
GET /products/paginate: Retrieve products with pagination.
GET /products/search: Search for products based on specific criteria.
GET /products/paginate_search: Search for products with pagination.
GET /products/top_selling: Retrieve the top-selling products based on total quantity ordered.
GET /products/production_efficiency: Evaluate the production efficiency of products based on specific dates.

Order Management

Blueprint: order_blueprint
URL Prefix: /orders

POST /orders/: Save a new order.
GET /orders/: Retrieve all orders.
GET /orders/int:id: Retrieve a specific order by ID.
GET /orders/customer/int:id: Retrieve orders by customer ID.
POST /orders/customer/email: Retrieve orders by customer email.
GET /orders/paginate: Retrieve orders with pagination.

Employee Management

Blueprint: employee_blueprint
URL Prefix: /employees

POST /employees/: Save a new employee.
GET /employees/: Retrieve all employees.
GET /employees/calc: Calculate the total quantity of products produced by each employee.

Some other routes implemented:

 
    http://127.0.0.1:5000/products/top_selling
    http://127.0.0.1:5000/orders
    http://127.0.0.1:5000/products/paginate?page=2&per_page=3
    http://127.0.0.1:5000/products/paginate_search?page=2&per_page=2&search=hair
    http://127.0.0.1:5000/customers/login
    http://127.0.0.1:5000/customers
    
    http://127.0.0.1:5000/customers/lifetime_value?threshold=20
    
    http://127.0.0.1:5000/products/production_efficiency?specific_date=2024-03-03
    
Key Features

Pagination

Pagination is implemented for both orders and products to efficiently handle large datasets. The endpoints /orders/paginate and /products/paginate allow for fetching data in smaller, manageable chunks, improving performance and user experience.

Advanced Querying

The system supports advanced querying features, such as:

Top-Selling Products: The /products/top_selling endpoint calculates and retrieves the top-selling products based on the total quantity ordered.
Customer Lifetime Value: The /customers/lifetime_value endpoint calculates the total value of orders placed by each customer.
Production Efficiency: The /products/production_efficiency endpoint evaluates the production efficiency by calculating the total quantity produced for each product on a specific date.

Blueprint Configuration
In app.py, the blueprints for each module are registered with URL prefixes as follows:

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(employee_blueprint, url_prefix='/employees')

Getting Started

Clone the repository:

git clone <repository-url>
cd factory-management-system
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
flask run
Access the API:
The API will be available at http://127.0.0.1:5000/ with routes accessible under /customers, /products, /orders, and /employees.

Testing
To test the implemented endpoints, you can use tools like Postman or cURL to send requests to the API and verify the responses.

Conclusion
This Factory Management System provides a comprehensive solution for managing factory operations, including customer management, product tracking, order processing, and employee performance evaluation. With the added features of pagination and advanced querying, the system is optimized for handling large datasets and extracting valuable insights.