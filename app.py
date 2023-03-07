from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.user import users
from utils.db import db

app = Flask(__name__,)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:3138533232@localhost/falabella'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(users)
