from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_fruit(self):
        fruits = [b'apple', b'orange', b'papaya', b'grape', b'banana', b'guava', b'kiwi', b'mango']
        response = self.client.get(url_for('fruits'))
        self.assertIn(response.data, fruits)
