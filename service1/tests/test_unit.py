from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app, db, Win


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@35.203.177.146/testdb',
                          SECRET_KEY='IT_IS_A_SECRET_KEY', DEBUG=True)
        return app

    def setUp(self):
        db.drop_all()
        db.create_all()

    # sample data
        test_win = Win(name="Mariam", fruit="kiwi",
                       prize="Versace Bright Crystal")
        db.session.add(test_win)
        db.session.commit()

    def tearDown(self):
        db.drop_all()


class TestViews(TestBase):
    def test_view(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)


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
