from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app, db, Win


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='mysql+pymysql://alimatea7:root@localhost/testdb',
                          SECRET_KEY='IT_IS_A_SECRET_KEY',
                          DEBUG=True
                          )
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


class TestResponse(TestBase):
    def test_values_on_page(self):
        with patch("requests.get") as g:
            with patch("requests.get") as f:
                with patch("requests.post") as p:
                    g.return_value.text = "Mariam"
                    f.return_value.text = "kiwi"
                    p.return_value.text = "Versace Bright Crystal"

                    response = self.client.get(url_for('index'))
                    self.assertEqual(response.status_code, 200)
