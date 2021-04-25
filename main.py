import os
import secrets

import pytz
from flask import Flask, render_template
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# init
app = Flask(__name__)
app.config.from_pyfile('config.py')

# extensions
db = SQLAlchemy(app)
auth = HTTPTokenAuth(scheme='Bearer')


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(32))


class Pool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, nullable=False)
    water_temp = db.Column(db.Float, nullable=False)
    last_update = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

def datetimefilter(value, format="%m-%d-%y %I:%M %p"):
    tz = pytz.timezone('US/Eastern') # timezone you want to convert to from UTC
    utc = pytz.timezone('UTC')
    value = utc.localize(value, is_dst=None).astimezone(pytz.utc)
    local_dt = value.astimezone(tz)
    return local_dt.strftime(format)


app.jinja_env.filters['datetimefilter'] = datetimefilter


@app.cli.command("create-token")
def create_token():
    generated_token = secrets.token_urlsafe(32)
    token = Token(key=generated_token)
    db.session.add(token)
    db.session.commit()
    print(generated_token)
    return


@app.cli.command("revoke-tokens")
def revoke_tokens():
    all_tokens = Token.query.all()
    for t in all_tokens:
        db.session.delete(t)
    db.session.commit()


@auth.verify_token
def verify_token(token):
    all_tokens = Token.query.filter_by(key=token).first()
    if all_tokens:
        return token


@app.route('/')
def index():
    pool = Pool.query.first()
    print(pool.last_update)
    return render_template('index.html', pool=pool)


@app.route('/splash', methods=['POST'])
@auth.login_required
def splash():
    pool = Pool(status=True, temp='99')
    db.session.add(pool)
    db.session.commit()
    return "Done"


if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db.create_all()
        pool = Pool(status=False, water_temp='0')
        db.session.add(pool)
        db.session.commit()
    app.run(debug=True)
