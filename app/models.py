from datetime import datetime
from app import db


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(32))


class Pool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, nullable=False)
    water_temp = db.Column(db.Float, nullable=False)
    uv_level = db.Column(db.String(5), nullable=False)
    uv_time = db.Column(db.Integer, nullable=False)
    weather_conditions = db.Column(db.String(255), nullable=False)
    outside_temp = db.Column(db.Float, nullable=False)
    last_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
