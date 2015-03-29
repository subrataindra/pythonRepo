from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']= True

db=SQLAlchemy(app)

class persons(db.Model):
	__tablename__='persons'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(64),unique=True)
	phone=db.Column(db.Integer)
	address=db.Column(db.String(100))

	def __repr__(self):
		return '<persons %r>' % self.name

db.create_all()


