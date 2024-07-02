from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Questions(db.Model):
    __table_args__ = {"schema":"homeassigment"}
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(4096), nullable=False)
    answer = db.Column(db.String(4096), nullable=False)
    timestamp = db.Column(db.DateTime, nullable = True)

    def __init__(self, question, answer, timestamp):
        self.question = question
        self.answer = answer
        self.timestamp = timestamp
