from flask import Flask, request
from OpenAIClient import OpenAIClient
import config

AIClient = OpenAIClient(config.OPEN_AI_SECRET_KEY)
app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    # get request json
    request_data = request.json
    
    # check if json has question key, if it doesnt dont do anything
    if 'question' in request_data:
        # get question
        question = request_data['question']
        answer = AIClient.ask(question)
        print(question, answer)
        # TODO: save question and answer to DB 
        
    # dont return anything as it was not specified in the assignment
    return ""

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)