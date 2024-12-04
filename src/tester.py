import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from testdbAPI import app  # Replace with the actual filename of your app

# Sample fraud data for testing
fraud_data = [
    {"fraud_id": 1, "transaction_id": 655, "fraud_detected_date": "4/10/2020 19:09", "fraud_type": "Skimming", "investigation_status":"Open", "fraud_resolution": "No Action Taken"},
    {"fraud_id": 2, "transaction_id": 251, "fraud_detected_date": "2/12/2021 7:47","fraud_type": "Stolen Card", "investigation_status":"Under Investigation", "fraud_resolution": "No Action Taken"}
]

# setUp: Initializes the test client so that it can send HTTP requests to the Flask app.
class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        """Set up the test client for the Flask app."""
        self.client = app.test_client()
        self.client.testing = True

# Test specific fraud record retrieval
    @patch('testdbAPI.fraud', fraud_data)
    def test_get_single_record(self):
        """Test getting a specific fraud record by ID."""
        record_id = 1
        response = self.client.get(f'/data/{record_id}')  # Assume endpoint handles /data/<id>
        
        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the response matches the expected record
        response_data = response.get_json()
        expected_data = {"id": 1, "name": "John Doe", "fraud_score": 99}
        self.assertEqual(response_data, expected_data)


if __name__ == '__main__':
    unittest.main()
