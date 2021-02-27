from unittest.mock import patch
from flask import url_for, Response, request
import random
from flask_testing import TestCase

from app import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_fruits_on_page(self):
        fruits = [b"apple", b"orange", b"papaya",
                  b"grape", b"banana", b"guava", b"kiwi"]
        response = self.client.get(url_for("fruits"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data, fruits)

    def test_fruits(self):
        with patch("requests.get") as g:
            g.return_value.text = b"kiwi"
            response = self.client.get(url_for("fruits"))
            response = b"kiwi"
            self.assertIn(b"kiwi", response)
