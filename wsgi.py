# wsgi.py
from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World and Pierre!"


@app.route('/api/v1/products')
def api_rest():
    PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'testit' }
    ]
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:product_id>')
def show_product(product_id):
    PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'testit' }
    ]
    for product in PRODUCTS:
        if product["id"] == product_id:
            return jsonify(product)
    return ('', 404)

@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'testit' }
    ]
    for product in PRODUCTS:
        if product["id"] == product_id:
            PRODUCTS.remove(product)
            return ('', 204)
    abort(404)

@app.route('/api/v1/products', methods=['POST'])
def create_product():
    id = Counter()
    next_id = id.next()
    new_product = { 'id':next_id, 'name':'Workelo'}
    return (jsonify(new_product), 201)

@app.route('/api/v1/products/<int:product_id>', methods=['PATCH'])
def update_product(product_id):
    new_name = "Hello !" # to test if the supplied name is empty, replace this by ""
    PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'testit' }
    ]
    if not new_name:
        return ('', 422)
    for product in PRODUCTS:
        if product["id"] == product_id:
            product["name"]=new_name
            return ('', 204)
    return ('', 422)


class Counter:
    def __init__(self):
        self.id = 3

    def next(self):
        self.id += 1
        return self.id

