from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app, db, Win


class TestBase(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Win(name="Mariam", fruit="kiwi",
                           prize="Versace Bright Crystal"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_view(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 500)


class TestResponse(TestBase):
    def test_values(self):
        with requests_mock.mock() as g:
            g.get("http://35.247.11.109:5001/names", text="Mariam")
            g.get("http://35.247.11.109:5002/fruits", text="kiwi")
            g.post("http://35.247.11.109:5003/prize",
                   text="Versace Bright Crystal")

            response = self.client.get(url_for('index'))
            self.assertIn(b'Mariam', response.data)
            self.assertIn(b'kiwi', response.data)
            self.assertIn(b'Versace Bright Crystal', response.data)
