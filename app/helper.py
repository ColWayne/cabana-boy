from app import app
import pytz


def datetimefilter(value, format="%m-%d-%y %I:%M %p"):
    tz = pytz.timezone('US/Eastern')  # timezone you want to convert to from UTC
    utc = pytz.timezone('UTC')
    value = utc.localize(value, is_dst=None).astimezone(pytz.utc)
    local_dt = value.astimezone(tz)
    return local_dt.strftime(format)


app.jinja_env.filters['datetimefilter'] = datetimefilter
