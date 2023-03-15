from enum import unique
from main.extensions import db
from main.shared.base_model import BaseModel, HasCreatedAt


class User(BaseModel, HasCreatedAt):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    userName = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    phoneNumber = db.Column(db.String, nullable=False)
    Store = db.Column(db.String, nullable=False)
    # receipts = db.relationship('Receipt')