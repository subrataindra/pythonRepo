from datetime import datetime

from app import db

class persons(db.Model):
	__tablename__='persons'
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(64),unique=True)
	phone=db.Column(db.Integer)
	address=db.Column(db.String(100))

	def __repr__(self):
		return '<persons %r>' % self.name

