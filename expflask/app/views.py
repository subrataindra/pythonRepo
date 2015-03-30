from app import app, db,  mail
from app.models import persons
from app.forms import NameForm, addForm, addUserForm
#from app.tree import Tree
from flask import render_template, request, redirect, url_for, flash
#from flask.ext.admin.contrib import sqla
from flask_mail import Message


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
