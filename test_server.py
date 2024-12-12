import unittest
from server import app  # Import the Flask app from your server code

class FlaskServerTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client for the Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_home_endpoint(self):
        # Test the root endpoint
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Welcome to my Web Server!")

    def test_greet_endpoint(self):
        # Test the dynamic greet endpoint
        response = self.app.get('/greet/Alice')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, Alice!")

    def test_add_endpoint(self):
        # Test the add endpoint with query parameters
        response = self.app.get('/add?num1=5&num2=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 8})

    def test_add_endpoint_invalid(self):
        # Test the add endpoint with invalid parameters
        response = self.app.get('/add?num1=abc&num2=3')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Invalid numbers provided"})

    def test_postdata_endpoint(self):
        # Test the POST data endpoint
        response = self.app.post('/postdata', json={"key": "value", "example": "data"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "received": {"key": "value", "example": "data"},
            "message": "Data received successfully!"
        })

if __name__ == '__main__':
    unittest.main()
