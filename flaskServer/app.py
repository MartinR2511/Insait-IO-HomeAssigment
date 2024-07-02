from flask import Flask, request
from OpenAIClient import OpenAIClient
from models import db, Questions
from datetime import datetime
import config

AIClient = OpenAIClient(config.OPEN_AI_SECRET_KEY)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@{ipaddress}:{port}/{database_name}'.format(username=config.DB_USERNAME, password=config.DB_PASSWORD, ipaddress=config.DB_IPADDRESS, port=config.DB_PORT, database_name=config.DB_NAME)
db.init_app(app)
    
@app.route("/ask", methods=["POST"])
def ask():
    # get request json
    timestamp = datetime.now()
    request_data = request.json
    
    # check if json has question key, if it doesnt dont do anything
    if 'question' in request_data:
        # get question
        question = request_data['question']
        answer = AIClient.ask(question)
        print(question, answer)
        row = Questions(question, answer, timestamp)
        db.session.add(row)
        db.session.commit()
        
    # dont return anything as it was not specified in the assignment
    return ""

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)