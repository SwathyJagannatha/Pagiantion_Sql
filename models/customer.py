from database import db,Base
from sqlalchemy.orm import Mapped,mapped_column
from typing import List
from models.role import Role

class Customer(Base):
    __tablename__ = 'Customers'
    id : Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(db.String(255),nullable=False)
    email : Mapped[str] = mapped_column(db.String(255),nullable=False,unique=True)
    phone: Mapped[str] = mapped_column(db.String(20),nullable=False)
    username : Mapped[str] = mapped_column(db.String(255),nullable=False)
    password: Mapped[str] = mapped_column(db.String(255),nullable=False)
    
    orders: Mapped[List["Order"]] = db.relationship(back_populates="customer")
    role: Mapped["Role"] = db.relationship("Role")
    role_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('Roles.id'), nullable=False)