from app import app
from models import db, Users

data =[
    {"name": "admin", "email": "admin.com.vn", "password": "123"},
]

with app.app_context():
    db.create_all() 
    for item in data:
        user = Users(name=item["name"], email=item["email"], password=item["password"])
        db.session.add(user)
    db.session.commit()
    print("data _user ok")