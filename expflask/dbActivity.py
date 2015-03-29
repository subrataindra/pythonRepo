from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask import Flask
from dbCreate import persons


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']= True

db=SQLAlchemy(app)

amit=persons(name='Ankur', phone='9830098300',address='mumbai')
subrata=persons(name='Mandar', phone='9830098300',address='kolkata')

db.session.add(amit)
db.session.add(subrata)

db.session.commit()

persons.query.all()