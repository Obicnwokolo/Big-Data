import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from testdbAPI import app  # Replace with the actual filename of your app


# setUp: Initializes the test client so that it can send HTTP requests to the Flask app.
class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        """Set up the test client for the Flask app."""
        self.client = app.test_client()
        self.client.testing = True

    def test_no_data(self):
        """Test the /data endpoint when there is no data."""
        # Assuming you can mock the fraud_data being empty
        global data
        data = []  # Set the fraud data to an empty list for this test
        
        # Make a GET request to the /data endpoint
        response = self.client.get('/data')
        
        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the response returns an empty list
        self.assertEqual(response.get_json(), [])
        #print(response.get_json())



if __name__ == '__main__':
    unittest.main()
