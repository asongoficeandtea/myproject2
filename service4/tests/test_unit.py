from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_prize(self):
        with patch("requests.post") as m:
            m.return_value.text = "Mariam"

            response = self.client.post(url_for('prize'), data='Mariam')
            self.assertEqual(response.status_code, 200)

