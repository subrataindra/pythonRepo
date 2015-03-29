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

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = 'supersecretkey'
#app.config['SECRET_KEY']='guess hard'
#app.config['SESSION_TYPE'] = 'filesystem'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']= True

db=SQLAlchemy(app)
bootstrap=Bootstrap(app)



#=======================

class NameForm(Form):
	fld1 = HiddenField("Field 1")
	edit=SubmitField('Edit')
	delete=SubmitField('Delete')



class addForm(Form):
	#name=StringField('Enter Name ', validators=[Required()])
	#phone=StringField('Enter Phone  ', validators=[Required()])
	#address=StringField('Enter Address ', validators=[Required()])
	add=SubmitField('Add')

class addUserForm(Form):
	name=StringField('Enter Name ', validators=[Required()])
	phone=StringField('Enter Phone  ', validators=[Required()])
	address=StringField('Enter Address ', validators=[Required()])
	addUser=SubmitField('Add')
	cancel=SubmitField('Cancel')
	
#========================


@app.route('/all', methods=['GET','POST'])
def all():
	all=persons.query.all()
	return render_template('/all.html', all=all)

@app.route('/allb', methods=['GET','POST'])
def allb():
	all=persons.query.all()
	x=NameForm(request.form)	
	adf=addForm(request.form)
	auf=addUserForm(request.form)

	print('data ',x.edit.data,adf.add.data)
	if request.method == 'POST' and x.validate() and x.edit.data:
		print('hidden data ',x.fld1.data)
		session['editUser']=x.fld1.data
		return redirect('/editUser')

	if request.method == 'POST' and x.validate() and x.delete.data:
		print('hidden data ',x.fld1.data)
		session['editUser']=x.fld1.data
		db.session.query(persons).filter_by(id=session['editUser']).delete()
		db.session.commit()
		all=persons.query.all()
		return render_template('/allbnew.html', all=all,x=x,adf=adf)

	#print(x.errors)
	if request.method == 'POST' and adf.validate()  and adf.add.data:
		return redirect('/addUser')

	
	return render_template('/allbnew.html', all=all,x=x,adf=adf)



@app.route('/addUser', methods=['GET','POST'])
def addUser():
	auf=addUserForm(request.form)
	
	if request.method == 'POST' and auf.validate() and auf.addUser.data:
		newUser=persons(name=auf.name.data, phone=auf.phone.data,address=auf.address.data)
		db.session.add(newUser)
		db.session.commit()
		flash('New User Added.')
		all=persons.query.all()
		return render_template('/all.html', all=all)
	
	return render_template('/addUser.html', auf=auf)



@app.route('/editUser', methods=['GET','POST'])
def editUser():
	ae=addUserForm(request.form)
	print(session['editUser'])
	sel=persons.query.filter_by(id=session['editUser']).all()

	if request.method == 'POST' and ae.validate() and ae.addUser.data:
		print('name ',ae.name.data,' phone ',ae.phone.data,' address ',ae.address.data)
		db.session.query(persons).filter_by(id=session['editUser']).update({ 'name': ae.name.data})
		db.session.query(persons).filter_by(id=session['editUser']).update({ 'phone': ae.phone.data})
		db.session.query(persons).filter_by(id=session['editUser']).update({ 'address': ae.address.data})
		db.session.commit()
		flash('User Edited.')
		all=persons.query.all()
		return render_template('/all.html', all=all)

		
	return render_template('editUser.html', ae=ae, sel=sel)


if __name__=='__main__':	
	app.run(host="127.0.0.1", port=int("5000"), debug=True)
	