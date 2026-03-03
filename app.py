from flask import Flask
from config import Config
from models import db, Vocabulary

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def home():
    return "app run" 
if __name__ == '__main__':
    app.run(debug=True)
