__author__ = 'jwogrady'

import os

basedir = os.path.abspath((os.path.dirname(__file__)))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'expFlask.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


SECRET_KEY = "supersecretkey"


MAIL_SERVER = 'smtp-relay.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_DEBUG = True
DEBUG = True
MAIL_SUPPRESS_SEND = False
TESTING = False
MAIL_USERNAME = False
MAIL_PASSWORD = False