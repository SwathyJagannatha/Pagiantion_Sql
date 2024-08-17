from database import db,Base
from sqlalchemy.orm import Mapped,mapped_column
from models.employeeProduct import employee_product

from typing import List

class Employee(Base):
    __tablename__ = 'Employees'
    id : Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(db.String(255),nullable=False)
    email : Mapped[str] = mapped_column(db.String(255),nullable=False,unique=True)
    phone: Mapped[str] = mapped_column(db.String(20),nullable=False)

    #Many to many
    products : Mapped[List['Product']] = db.relationship(secondary=employee_product)