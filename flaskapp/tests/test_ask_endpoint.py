
"""
This file contains test cases for the '/ask' endpoint of the Flask application.
The '/ask' endpoint is responsible for processing questions and returning answers.
"""
from app import app


def test_correct_input():
    """
    Test case to check the behavior of the '/ask' endpoint when provided with a correct input.
    """
    with app.test_client() as client:
        response = client.post('/ask', json={'question': 'What is the capital of France?'})
        assert response.status_code == 200
        assert len(response.json['answer']) > 0

def test_empty_question():
    """
    Test case to check the behavior of the '/ask' endpoint when provided with an empty question.
    """
    with app.test_client() as client:
        response = client.post('/ask', json={'question': ''})
        assert response.status_code == 400
        assert response.json['error'] == 'Question cannot be empty'

def test_no_question_in_json():
    """
    Test case to check the behavior of the '/ask' endpoint when the 'question' key is missing in the JSON payload.
    """
    with app.test_client() as client:
        response = client.post('/ask', json={'other': 'other'})
        assert response.status_code == 400
        assert response.json['error'] == 'Question is required'

def test_text_as_json_input():
    """
    Test case to check the behavior of the '/ask' endpoint when provided with non-JSON data but with JSON data header.
    """
    with app.test_client() as client:
        response = client.post('/ask', data='not json', headers={'Content-Type': 'application/json'})
        assert response.status_code == 400
        assert response.json['error'] == 'Request data is not JSON'

def test_not_json_input():
    """
    Test case to check the behavior of the '/ask' endpoint when provided with non-JSON data.
    """
    with app.test_client() as client:
        response = client.post('/ask', data='not json')
        assert response.status_code == 400
        assert response.json['error'] == 'Request data is not JSON'

def test_no_data():
    """
    Test case to check the behavior of the '/ask' endpoint when no data is provided in the request.
    """
    with app.test_client() as client:
        response = client.post('/ask')
        assert response.status_code == 400
        assert response.json['error'] == 'Request data is not JSON'