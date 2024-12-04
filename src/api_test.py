import unittest
from flask import Flask, jsonify, request

from testdbAPI import app

class TestAPIconnection(unittest.TestCase):
    def setUp(self):
        """Set up the test client for the Flask app."""
        self.client=app.test_client()
        self.client.testing = True


if __name__ == 'main':
    unittest.main