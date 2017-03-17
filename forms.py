from flask.ext.wtf import FlaskForm
from wtforms.fields import TextField, TextAreaField, SubmitField
from wtforms import validators, ValidationError
 
class ContactForm(FlaskForm):
  name = TextField("Name",  [validators.Required()])
  email = TextField("Email",  [validators.Required()])
  subject = TextField("Subject",  [validators.Required()])
  message = TextAreaField("Message",  [validators.Required()])
  submit = SubmitField("Send")
