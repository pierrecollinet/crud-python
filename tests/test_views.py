# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_product_exists(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        response = self.client.get("/api/v1/products/2")
        product = response.data.decode()
        self.assertEqual(response.status_code, 200)

    def test_product_not_exist(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        response = self.client.get("/api/v1/products/9")
        product = response.data.decode()
        self.assertEqual(response.status_code, 404)

    def test_product_not_exists_delete(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        response = self.client.delete("/api/v1/products/9")
        product = response.data.decode()
        self.assertEqual(response.status_code, 404)

    def test_product_exists_delete(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        response = self.client.delete("/api/v1/products/2")
        product = response.data.decode()
        self.assertEqual(response.status_code, 204)

    def test_product_create(self):
        response = self.client.post("/api/v1/products")
        product = response.data.decode()
        self.assertEqual(response.status_code, 201)

    def test_product_update(self):
        response = self.client.patch("/api/v1/products/2")
        self.assertEqual(response.status_code, 204)

    # in WSGI give new_name, the value ""
    # def test_product_update_empty_name(self):
    #     response = self.client.patch("/api/v1/products/2")
    #     self.assertEqual(response.status_code, 422)


