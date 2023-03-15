from enum import unique
from main.extensions import db
from main.shared.base_model import BaseModel, HasCreatedAt


class Admin(BaseModel, HasCreatedAt):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    adminName = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(25), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    Store = db.Column(db.String(20), nullable=False)
