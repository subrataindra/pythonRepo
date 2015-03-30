from flask.ext.wtf import Form
from wtforms import SubmitField,StringField,HiddenField
from wtforms.validators import Required

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
