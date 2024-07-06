
"""
This file contains tests for the models of the flaskapp.
"""

from flaskapp.models import Questions

def test_questions():
    """
    Test the questions model.
    """
    question = Questions('What is the capital of France?', 'Paris', '2020-01-01 00:00:00', '192.168.1.5')
    assert question.question == 'What is the capital of France?'
    assert question.answer == 'Paris'
    assert question.timestamp == '2020-01-01 00:00:00'
    assert question.ipaddress == '192.168.1.5'