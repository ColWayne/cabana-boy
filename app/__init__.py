import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
auth = HTTPTokenAuth(scheme='Bearer')
migrate = Migrate(app, db)


if not os.path.exists('db.sqlite'):
    db.create_all()

from app import routes, cli, models