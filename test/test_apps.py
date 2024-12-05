import unittest
from flask import Flask, jsonify
from testdbAPI import app  # Replace with the actual filename of your app

# setUp: Initializes the test client so that it can send HTTP requests to the Flask app.
class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        """Set up the test client for the Flask app."""
        self.client = app.test_client()
        self.client.testing = True # ensures detailed error messages are displayed incase of any issues.

# Test that data is returned successfully
    def test_get_data(self):
        """Test the /data endpoint."""
        response = self.client.get('/data') # Make a GET request to the /data endpoint
        self.assertEqual(response.status_code, 200) # Check if the status code is 200 (OK)
        self.assertEqual(response.content_type, 'application/json') # Check if the response is in JSON format 
        data = response.get_json() # Check if the response contains some expected data
        self.assertIsInstance(data, list) # Assuming the fraud_data has at least one record, check if the response has a list
        
        # Check if the data contains expected keys (e.g., "fraud_id")
        if data:  # Check if the list is not empty
            self.assertIn('fraud_id', data[0])  # Replace 'fraud_id' with a valid column name



if __name__ == '__main__':
    unittest.main()