from database import db,Base
from typing import List
from sqlalchemy.orm import Mapped,mapped_column
from models.orderProduct import order_product

class Order(Base):
    __tablename__ = 'Orders'
    id : Mapped[int] = mapped_column(primary_key = True)
    date: Mapped[str] = mapped_column(db.Date,nullable=False)
    customer_id : Mapped[int] = mapped_column(db.ForeignKey('Customers.id'))
   
   # Many to one
    customer : Mapped['Customer'] = db.relationship(back_populates = "orders")

    #Many to many
    products : Mapped[List['Product']] = db.relationship(secondary=order_product)