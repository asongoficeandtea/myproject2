from unittest.mock import patch
from flask import url_for
import string
from flask_testing import TestCase

from app import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):
    def test_prize(self):
        response = self.client.post(
            url_for("prize"), json={"names": "Mariam", "fruits": "kiwi"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data, [b"Roberto Cavalli Oud al-Qasr", b"Black Phantom by Kilian", b"Versace Bright Crystal", b"Gucci Guilty", b"Byredo Gypsy Water", b"Maison Francis Kurkdjian Baccarat Rouge 540",
                                      b"Maison Margiela Replica By the Fire", b"Jo Malone London Velvet Rose and Oud", b"Kay Ali Vanilla 28", b"Kilian Rolling in Love"]

                      )
