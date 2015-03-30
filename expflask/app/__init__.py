from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask import Flask,render_template
from dbCreate import persons
from flask.ext.wtf import Form
from wtforms import SubmitField,StringField,HiddenField
from wtforms.validators import Required
from flask.ext.bootstrap import Bootstrap
from flask import request,redirect,flash,url_for, session
from flask.ext.session import Session
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
#from flask.ext.admin import Admin
from flask_mail import Mail


app = Flask(__name__)
#app.secret_key = 'supersecretkey'
app.config.from_object('config')
#app.config['SECRET_KEY']='guess hard'
#app.config['SESSION_TYPE'] = 'filesystem'

#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']= True

db=SQLAlchemy(app)
migrate = Migrate(app,db)


manager=Manager(app)
manager.add_command('db',MigrateCommand)

bootstrap=Bootstrap(app)
#admin=Admin(app)
mail=Mail(app)

from app import views, models, forms

