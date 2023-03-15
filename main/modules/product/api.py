from flask import Blueprint
from flask import json
from flask.globals import request
from flask.json import jsonify
import uuid
from werkzeug.utils import secure_filename
from main.modules.product.models import Product
from main.modules.product.schema import ProductSchema
from datetime import datetime
import os
import http

blueprint = Blueprint('product', __name__, url_prefix='/api')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg', 'gif']


@blueprint.route('/products', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def api_root():
    if request.method == 'GET':
        products = Product.query.filter_by(Store='OYAStore').all()
        pList = []
        for product in products:
            pList.append(ProductSchema().dump(product))
        return jsonify({
            "products": pList
        }), http.HTTPStatus.OK
    if request.method == 'POST':
        form_data = (request.json or (request.form.to_dict()
                     if request.form else None)) or {}
        error = []
        try:
            imgOb = request.files['imgOb']
        except:
            error.append("please enter an image 'imgOb'")
        try:
            form_data['quantity']
        except:
            error.append("please enter a quantity")
        else:
            if form_data['quantity'] == "" or form_data['quantity'].isspace():
                error.append("please enter a quantity")
            else:
                try:
                    form_data['quantity'] = int(form_data['quantity'])
                except:
                    error.append("the quantity must be an integer")
        try:
            form_data['price']
        except:
            error.append("please enter a price")
        else:
            if form_data['price'] == "" or form_data['price'].isspace():
                error.append("please enter a price")
            else:
                try:
                    form_data['price'] = int(form_data['price'])
                except:
                    error.append("the price must be an integer")
        try:
            form_data['title']
        except:
            error.append("please enter a title")
        else:
            if form_data['title'] == "" or form_data['title'].isspace():
                error.append("please enter a title")
        try:
            form_data['description']
        except:
            error.append("please enter a description")
        else:
            if form_data['description'] == "" or form_data['description'].isspace():
                error.append("please enter a description")
        try:
            form_data['category']
        except:
            error.append("please enter a category")
        else:
            if form_data['category'] == "" or form_data['category'].isspace():
                error.append("please enter a category")
        if not error == []:
            return jsonify({
                "error": error
            }), http.HTTPStatus.BAD_REQUEST
        if imgOb:
            if not allowed_file(imgOb.filename):
                return jsonify({
                    "error": "the type of file imgOb is not suitable ",
                    "suitable extensions": "png, jpg, jpeg, gif"
                }), http.HTTPStatus.BAD_REQUEST
            try:
                img1 = request.files['img1']
            except:
                img1 = None
            try:
                img2 = request.files['img2']
            except:
                img2 = None
            if img1:
                if not allowed_file(img1.filename):
                    return jsonify({
                        "error": "the type of file img1 is not suitable ",
                        "suitable extensions": "png, jpg, jpeg, gif"
                    }), http.HTTPStatus.BAD_REQUEST
                if img2:
                    if not allowed_file(img2.filename):
                        return jsonify({
                            "error": "the type of file img2 is not suitable ",
                            "suitable extensions": "png, jpg, jpeg, gif"
                        }), http.HTTPStatus.BAD_REQUEST
                    filenameOb = str(uuid.uuid4()) + '.' + \
                        imgOb.filename.rsplit('.', 1)[1].lower()
                    filenameOb = secure_filename(filenameOb)
                    imgOb.save(os.path.join(
                        os.getcwd(), 'uploads', '', filenameOb))
                    filename1 = str(uuid.uuid4()) + '.' + \
                        img1.filename.rsplit('.', 1)[1].lower()
                    filename1 = secure_filename(filename1)
                    img1.save(os.path.join(
                        os.getcwd(), 'uploads', '', filename1))
                    filename2 = str(uuid.uuid4()) + '.' + \
                        img2.filename.rsplit('.', 1)[1].lower()
                    filename2 = secure_filename(filename2)
                    img2.save(os.path.join(
                        os.getcwd(), 'uploads', '', filename2))
                    product = Product(title=form_data['title'], description=form_data['description'], date=datetime.today().strftime(
                        '%Y-%m-%d'), category=form_data['category'], price=form_data['price'], quantity=form_data['quantity'], Store="OYAStore", imgOb=filenameOb, img1=filename1, img2=filename2, commit=True)
                    return jsonify({
                        "msg": "success"
                    }), http.HTTPStatus.CREATED
                else:
                    filenameOb = str(uuid.uuid4()) + '.' + \
                        imgOb.filename.rsplit('.', 1)[1].lower()
                    filenameOb = secure_filename(filenameOb)
                    imgOb.save(os.path.join(
                        os.getcwd(), 'uploads', '', filenameOb))
                    filename1 = str(uuid.uuid4()) + '.' + \
                        img1.filename.rsplit('.', 1)[1].lower()
                    filename1 = secure_filename(filename1)
                    img1.save(os.path.join(
                        os.getcwd(), 'uploads', '', filename1))
                    product = Product(title=form_data['title'], description=form_data['description'], date=datetime.today().strftime(
                        '%Y-%m-%d'), category=form_data['category'], price=form_data['price'], quantity=form_data['quantity'], Store="OYAStore", imgOb=filenameOb, img1=filename1, commit=True)
                    return jsonify({
                        "msg": "success"
                    }), http.HTTPStatus.CREATED
            else:
                if img2:
                    if not allowed_file(img2.filename):
                        return jsonify({
                            "error": "the type of file img2 is not suitable ",
                            "suitable extensions": "png, jpg, jpeg, gif"
                        }), http.HTTPStatus.BAD_REQUEST
                    filenameOb = str(uuid.uuid4()) + '.' + \
                        imgOb.filename.rsplit('.', 1)[1].lower()
                    filenameOb = secure_filename(filenameOb)
                    imgOb.save(os.path.join(
                        os.getcwd(), 'uploads', '', filenameOb))
                    filename2 = str(uuid.uuid4()) + '.' + \
                        img2.filename.rsplit('.', 1)[1].lower()
                    filename2 = secure_filename(filename2)
                    img2.save(os.path.join(
                        os.getcwd(), 'uploads', '', filename2))
                    product = Product(title=form_data['title'], description=form_data['description'], date=datetime.today().strftime(
                        '%Y-%m-%d'), category=form_data['category'], price=form_data['price'], quantity=form_data['quantity'], Store="OYAStore", imgOb=filenameOb, img2=filename2, commit=True)
                    return jsonify({
                        "msg": "success"
                    }), http.HTTPStatus.CREATED
                else:
                    filename = str(uuid.uuid4()) + '.' + \
                        imgOb.filename.rsplit('.', 1)[1].lower()
                    filename = secure_filename(filename)
                    imgOb.save(os.path.join(
                        os.getcwd(), 'uploads', '', filename))
                    product = Product(title=form_data['title'], description=form_data['description'], date=datetime.today().strftime(
                        '%Y-%m-%d'), category=form_data['category'], price=form_data['price'], quantity=form_data['quantity'], Store="OYAStore", imgOb=filename, commit=True)
                    return jsonify({"msg": "Success"}), http.HTTPStatus.CREATED
        else:
            return jsonify({
                "error": "no image selected for uploading"
            }), http.HTTPStatus.BAD_REQUEST
    if request.method == 'PATCH':
        form_data = (request.json or (request.form.to_dict()
                     if request.form else None)) or {}
        error = ""
        try:
            form_data['id']
        except:
            return jsonify({
                "error": "you didn't provide the id for the product you want to update"
            }), http.HTTPStatus.NOT_FOUND
        else:
            if form_data['id'] == "":
                return jsonify({"error": "you didn't provide the id for the product you want to update"}), http.HTTPStatus.NOT_FOUND
            else:
                try:
                    form_data['id'] = int(form_data['id'])
                except:
                    return jsonify({
                        "error": "the id must be an integer"
                    }), http.HTTPStatus.BAD_REQUEST
                else:
                    p = Product.query.filter_by(
                        id=form_data['id']).first()
                    if p:
                        updates = {}
                        try:
                            form_data['price']
                        except:
                            pass
                        else:
                            updates['price'] = int(form_data['price'])
                        try:
                            form_data['title']
                        except:
                            pass
                        else:
                            updates['title'] = form_data['title']
                        try:
                            form_data['quantity']
                        except:
                            pass
                        else:
                            updates['quantity'] = int(form_data['quantity'])
                        try:
                            form_data['category']
                        except:
                            pass
                        else:
                            updates['category'] = form_data['category']
                        try:
                            form_data['description']
                        except:
                            pass
                        else:
                            updates['description'] = form_data['description']
                        try:
                            imgOb = request.files['imgOb']
                        except:
                            pass
                        else:
                            if not allowed_file(imgOb.filename):
                                return jsonify({
                                    "error": "the type of file imgOb is not suitable ",
                                    "suitable extensions": "png, jpg, jpeg, gif"
                                }), 400
                            os.remove(os.path.join(
                                os.getcwd(), 'uploads', '', p.imgOb))
                            filename = str(uuid.uuid4()) + '.' + \
                                imgOb.filename.rsplit('.', 1)[1].lower()
                            filename = secure_filename(filename)
                            imgOb.save(os.path.join(
                                os.getcwd(), 'uploads', '', filename))
                            updates['imgOb'] = filename
                        try:
                            img1 = request.files['img1']
                        except:
                            pass
                        else:
                            if not allowed_file(img1.filename):
                                return jsonify({
                                    "error": "the type of file img1 is not suitable ",
                                    "suitable extensions": "png, jpg, jpeg, gif"
                                }), http.HTTPStatus.BAD_REQUEST
                            if p.img1:
                                os.remove(os.path.join(
                                    os.getcwd(), 'uploads', '', p.img1))
                            filename = str(uuid.uuid4()) + '.' + \
                                img1.filename.rsplit('.', 1)[1].lower()
                            filename = secure_filename(filename)
                            img1.save(os.path.join(
                                os.getcwd(), 'uploads', '', filename))
                            updates['img1'] = filename
                        try:
                            img2 = request.files['img2']
                        except:
                            pass
                        else:
                            if not allowed_file(img2.filename):
                                return jsonify({
                                    "error": "the type of file img2 is not suitable ",
                                    "suitable extensions": "png, jpg, jpeg, gif"
                                }), http.HTTPStatus.BAD_REQUEST
                            if p.img2:
                                os.remove(os.path.join(
                                    os.getcwd(), 'uploads', '', p.img2))
                            filename = str(uuid.uuid4()) + '.' + \
                                img2.filename.rsplit('.', 1)[1].lower()
                            filename = secure_filename(filename)
                            img2.save(os.path.join(
                                os.getcwd(), 'uploads', '', filename))
                            updates['img2'] = filename
                        if updates == {}:
                            return jsonify({"msg": "you didn't send anything to upgrade"}), http.HTTPStatus.BAD_REQUEST
                        else:
                            p.update(form_data=updates, commit=True)
                            return jsonify({"msg": "success"}), http.HTTPStatus.OK
                    else:
                        return jsonify({"error": "product not found in your data base"}), http.HTTPStatus.NOT_FOUND
    if request.method == 'DELETE':
        form_data = (request.json or (request.form.to_dict()
                     if request.form else None)) or {}
        try:
            form_data['id']
        except:
            return jsonify({
                "error": "you didn't send the id of the product you want to delete"
            }), http.HTTPStatus.BAD_REQUEST
        else:
            try:
                form_data['id'] = int(form_data['id'])
            except:
                return jsonify({'error': ' the id must be an integer'}), http.HTTPStatus.BAD_REQUEST
            else:
                p = Product.query.filter_by(id=form_data['id']).first()
                if p:
                    if p.img1:
                        os.remove(os.path.join(
                            os.getcwd(), 'uploads', '', p.img1))
                    if p.img2:
                        os.remove(os.path.join(
                            os.getcwd(), 'uploads', '', p.img2))
                    os.remove(os.path.join(
                        os.getcwd(), 'uploads', '', p.imgOb))
                    p.destroy(commit=True)
                    return jsonify({"msg": "element deleted successfully"}), http.HTTPStatus.OK
                else:
                    return jsonify({"error": "the element you want to delete doesn't exist in your data base"}), http.HTTPStatus.NOT_FOUND
