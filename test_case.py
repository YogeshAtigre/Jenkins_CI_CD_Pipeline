from app import app


def test_home():
    # Create a test client using the Flask application
    client = app.test_client()

    # Send a GET request to the root URL
    response = client.get('/')

    # Assert the response data and status code
    assert response.status_code == 200
    assert b'Hello, Jenkins CI/CD Pipeline with Flask Application!' in response.data
