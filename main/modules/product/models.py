from enum import unique
from main.extensions import db
from main.shared.base_model import BaseModel


class Product(BaseModel):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    Store = db.Column(db.String(25), nullable=False)
    imgOb = db.Column(db.String, nullable=False)
    img1 = db.Column(db.String)
    img2 = db.Column(db.String)
