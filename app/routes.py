from flask import render_template

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
    pool = Pool(status=True,
                water_temp='99',
                uv_level='Low',
                uv_time='25',
                weather_conditions='cloudy',
                outside_temp='98'
                )
    db.session.add(pool)
    db.session.commit()
    return "Done"
