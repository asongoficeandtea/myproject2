from unittest.mock import patch
import unittest
from flask import url_for, request
from flask_testing import TestCase
import requests_mock

from app import app, db, Win


class TestBase(TestCase):
    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        test_win = Win(name="Mariam", fruit="kiwi",
                       prize="Versace Bright Crystal")

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestResponse(TestBase):
    def test_data_on_page(self):
