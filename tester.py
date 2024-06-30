import requests

url = "http://127.0.0.1:5000/ask"
data = {"question": "what is the sum of 5,4,2,3,1?"}

response = requests.post(url, json=data)

print(response.text)