from database import db,Base
from sqlalchemy.orm import Mapped,mapped_column
from models.role import Role

class User(Base):
    __tablename__ = 'users'
    id : Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(db.String(255),nullable=False)
    email : Mapped[str] = mapped_column(db.String(255),nullable=False,unique=True)
    phone: Mapped[str] = mapped_column(db.String(255),nullable=False)
    username : Mapped[str] = mapped_column(db.String(255),nullable=False)
    password: Mapped[str] = mapped_column(db.String(255),nullable=False)
    
    #role
    role: Mapped["Role"] = db.relationship("Role")
    role_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('Roles.id'), nullable=False)
