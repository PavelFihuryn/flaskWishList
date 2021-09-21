import os


basedir = os.path.abspath(os.path.dirname(__file__))

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

a
class Configuration(object):
    DEBUG = True

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = 'static/uploads'



