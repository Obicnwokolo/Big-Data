import unittest
from flask import Flask, jsonify, request

from testdbAPI import app

class TestAPIconnection(unittest.TestCase):
    def setUp(self):
        """Set up the test client for the Flask app."""
        self.client=app.test_client()
        self.client.testing = True

def test_valid_request(self):
        """Test the API with valid input."""
        response = self.client.get('/your-endpoint?param1=value1&param2=value2')  # Replace with your API's endpoint and parameters
        self.assertEqual(response.status_code, 200)
        self.assertIn('expected_key', response.json)

if __name__ == '__main__':
    unittest.main()