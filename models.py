from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
class Vocabulary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word_jp = db.Column(db.String(10), nullable=False)
    word = db.Column(db.String(10), nullable=False)
    meaning = db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return f'<Vocabulary {self.word_jp}, {self.word}>'
    
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)