from flask import render_template, request
from datetime import datetime

from app import app, auth, db
from app.models import Pool
from app.helper import datetimefilter


@app.route('/')
@app.route('/index')
def index():
    pool = Pool.query.first_or_404()
    return render_template('index.html', pool=pool)


@app.route('/splash', methods=['POST'])
@auth.login_required
def splash():
    request_json = request.get_json()
    status = request_json.get('status')
    water_temp = request_json.get('water_temp')
    uv_level = request_json.get('uv_level')
    uv_time = request_json.get('uv_time')
    weather_conditions = request_json.get('weather_conditions')
    outside_temp = request_json.get('outside_temp')
    pool = Pool.query.first()
    if not pool:
        pool = Pool(status=status,
                    water_temp=water_temp,
                    uv_level=uv_level,
                    uv_time=uv_time,
                    weather_conditions=weather_conditions,
                    outside_temp=outside_temp
                    )
        db.session.add(pool)
    else:
        pool.status = status
        pool.water_temp = water_temp
        pool.uv_level = uv_level
        pool.uv_time = uv_time
        pool.weather_conditions = weather_conditions
        pool.outside_temp = outside_temp
        pool.last_update = datetime.utcnow()

    db.session.commit()
    return "Pool is " + str(status)
