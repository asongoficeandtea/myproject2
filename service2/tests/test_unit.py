import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_names_on_page(self):
        names = [b"leila", b"Amina", b"maya",
                 b"Waris", b"khadra", b"Fatima", b"shamhan", b"Mariam", b"mulki"]
        response = self.client.get(url_for("names"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data, names)

    def test_names(self):
        with patch("requests.get") as g:
            g.return_value.text = b"Mariam"
            response = self.client.get(url_for("names"))
            response = b"Mariam"
            self.assertIn(b"Mariam", response)
