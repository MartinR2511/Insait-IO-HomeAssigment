import requests
import json

# Define the URL and JSON data
url = 'http://localhost:5000/ask'
question = 'what is the capital of France?'
data = {
    'question': question,
}

# Send the POST request with JSON data
response = requests.post(url, json=data)

# Print the response
print(response.text)