from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask import Flask
from dbCreate import persons


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']= True

db=SQLAlchemy(app)

ankur=persons(name='Ankur')
kolkata=persons(address='kolkata')


all=persons.query.all()

sel=persons.query.filter_by(address='kolkata').all()

print(all)

for item in all:
	print('id = ', item.id)
	print('name = ',item.name)
	print('phone = ',item.phone)
	print('address = ',item.address)
	print('')

#print(sel[0].name)
#print(sel[0].phone)