from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_name(self):
        names = [b'leila', b'Amina', b'maya',
             b'Waris', b'khadra', b'Fatima', b'shamhan', b'Mariam', b'mulki']
        response = self.client.get(url_for('names'))
        self.assertIn(response.data, names)
