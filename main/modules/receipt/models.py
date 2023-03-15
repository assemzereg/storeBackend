from main.extensions import db
from main.shared.base_model import BaseModel, HasCreatedAt


class Receipt(BaseModel, HasCreatedAt):
    __tablename__ = 'receipts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    total = db.Column(db.Integer, nullable=False)
    Store = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    bought_products = db.relationship(
        'Bought_Product', cascade='all, delete-orphan')

    def __init__(self, form_data=None, commit=False, *args, **kwargs):
        if form_data:
            for key in list(form_data.keys()):
                if not hasattr(self, key):
                    form_data.pop(key)
                form_data.update(kwargs)
                kwargs = form_data
        BP = form_data.pop('bought_products')
        for b in BP:
            b['reciept_id'] = self.id
            bp = Bought_Product(b, commit=commit)
        self.bought_products.append(bp)
        super().__init__(*args, **kwargs)

    def update(self, form_data=None, commit=False, *args, **kwargs):
        if form_data:
            for key in list(form_data.keys()):
                if not hasattr(self, key):
                    form_data.pop(key)
                form_data.update(kwargs)
                kwargs = form_data
        BP = form_data.pop('bought_products')
        for b in BP:
            bp = Bought_Product.query.filter_by(id=b['id'])
            if bp:
                bp.update(form_data=b, commit=commit)
        super.update(*args, **kwargs)


class Bought_Product(BaseModel):
    __tablename__ = 'bought_products'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    receipt_id = db.Column(db.Integer, db.ForeignKey('receipts.id'))
