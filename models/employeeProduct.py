from database import db,Base 

# table for reelationship between product and employee, in place of Production table
employee_product = db.Table(
     'Employee_Product',
     Base.metadata,
     db.Column('employee_id',db.ForeignKey("Employees.id"),primary_key=True),
     db.Column('product_id',db.ForeignKey("Products.id"),primary_key=True),
     db.Column('quantity',db.Integer,nullable=False),
     db.Column('date',db.Date,nullable=False) # Production date
)