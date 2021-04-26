from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or \
        'sqlite:///' + path.join(basedir, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
