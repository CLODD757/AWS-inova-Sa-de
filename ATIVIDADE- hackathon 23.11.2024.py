Nova saúde/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── venv/
├── requirements.txt
└── run.py

Flask==2.0.3
Flask-SQLAlchemy==2.5.1
Flask-RESTful==0.3.9

from app import app

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

from app import routes
from app import app, db, api
from flask import request
from flask_restful import Resource
import uuid
class User(Resource):
def post(self):
data = request.get_json()
user_id = uuid.uuid4().hex
# Código para adicionar usuário ao banco de dados
return {"message": "Usuário cadastrado com sucesso", "user_id": user_id}, 201
api.add_resource(User, '/register')

