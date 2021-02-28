from flask import url_for
from flask_testing import TestCase
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestViews(TestBase):
    def test_prize_get(self):
        response = self.client.post(url_for('prize'))
        self.assertEqual(response.status_code, 200)

