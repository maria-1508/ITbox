from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Vocabulary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word_jp = db.Column(db.String(10), nullable=False)
    word = db.Column(db.String(10), nullable=False)
    meaning = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Vocabulary {self.word_jp}, {self.word}>'