from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from app import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_name(self):
        with patch("random.choice") as n:
            n.return_value = "Mariam"
            response = self.client.get(url_for('names'))
            self.assertEqual(b'Mariam', response.data)
