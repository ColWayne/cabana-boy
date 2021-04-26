from flask import render_template

from app import app
from app.models import Pool
from app.helper import datetimefilter


@app.route('/')
@app.route('/index')
def index():
    pool = Pool.query.first()
    return render_template('index.html', pool=pool)
