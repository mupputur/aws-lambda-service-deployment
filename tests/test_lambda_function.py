import unittest
from unittest.mock import patch
import json
from src.lambda_function import lambda_handler   

class TestLambdaHandler(unittest.TestCase):
    
    @patch('builtins.print')  # Mocking 'print' to prevent actual print statements in tests
    def test_customer_found(self, mock_print):
        # Input event with a valid customer ID
        event = {"id": 1}
        context = {}  # Mocked AWS Lambda context (not used here)
        
        response = lambda_handler(event, context)
        
        expected_response = {
            "statusCode": 200,
            "body": json.dumps({
                "id": 1,
                "email": "isidro_von@hotmail.com",
                "name": "Torrey Veum",
                "company": "Hilll, Mayert and Wolf"
            })
        }
        
        self.assertEqual(response, expected_response)
        mock_print.assert_called_with("Identified the customer id : 1 and processing data...")

    @patch('builtins.print')
    def test_customer_not_found(self, mock_print):
        # Input event with an invalid customer ID
        event = {"id": 999}
        context = {}

        response = lambda_handler(event, context)

        expected_response = {
            "statusCode": 404,
            "message": "customer 'id' not found"
        }

        self.assertEqual(response, expected_response)
        mock_print.assert_called_with("Customer id : 999 not found in database record")

    @patch('builtins.print')
    def test_error_handling(self, mock_print):
        # Input event with a missing 'id' key
        event = {}
        context = {}

        response = lambda_handler(event, context)

        expected_response = {
            "statusCode": 500,
            "message": "Internal Server"
        }

        self.assertEqual(response, expected_response)
        mock_print.assert_called_with("Error occured while processing customer data. ERROR: Invalid input: 'id' is required")

if __name__ == '__main__':
    unittest.main()
