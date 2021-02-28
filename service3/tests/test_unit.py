from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from app import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_fruit(self):
        with patch("random.choice") as f:
            f.return_value = "kiwi"
            response = self.client.get(url_for('fruits'))
            self.assertEqual(b'kiwi', response.data)
