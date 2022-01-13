from flask_wtf import Form
from wtforms import IntegerField, TextAreaField, SelectField, SubmitField, TextField, RadioField
from wtforms import validators


class ContactForm(Form):
    name = TextField("Name of Student", [validators.Required("Please enter name")])
    Gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    Address = TextAreaField('Address')
    email = TextField('Email', [validators.Required("Please enter your email")])
    Age = IntegerField('age')
    language = SelectField('Languages', choices=[('cpp', 'C++'), ('py', 'python')])
    submit = SubmitField('Send')
