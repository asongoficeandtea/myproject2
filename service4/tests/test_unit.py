from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_prize(self):
        response = self.client.post(url_for('prize'), data="Mariam")
        self.assertIn(b'Versace Bright Crystal', response.data)

    def test_another(self):
        response = self.client.post(url_for('prize'), data="mulki")
        self.assertIn(b'Porsche 911', response.data)
