from flask import Flask, request
from AIClients.OpenAIClient import OpenAIClient
from models import db, Questions
from datetime import datetime
import config

AIClient = OpenAIClient(config.OPEN_AI_SECRET_KEY)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@{ipaddress}:{port}/{database_name}'.format(username=config.DB_USERNAME, password=config.DB_PASSWORD, ipaddress=config.DB_IPADDRESS, port=config.DB_PORT, database_name=config.DB_NAME)
db.init_app(app)
    
@app.route("/ask", methods=["POST"])
def ask():
    # get timestamp of request
    timestamp = datetime.now()
    
    # check if request has and data and if it is json
    if not request.is_json:
        return {"error": "Request data is not JSON"}, 400
    
    # check if the question key is in the json
    try:
        if 'question' not in request.json:
            return {"error": "Question is required"}, 400
    except Exception :
        return {"error": "Request data is not JSON"}, 400
    
    # get question from json
    question = request.json['question']
    
    #check if question is empty
    if not question:
        return {"error": "Question cannot be empty"}, 400

    # get answer from AI
    answer = AIClient.ask(question)
    row = Questions(question, answer, timestamp)

    try:
        db.session.add(row)
        db.session.commit()
    except Exception as e:
        return {"error": "Internal server error"}, 500

    # return answer from AI and 200 status code        
    return {"answer": answer}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)