from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField
from wtforms import validators, EmailField
from email_validator import validate_email, EmailNotValidError

class UserForm(Form):
    matricula = StringField('Matricula', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=3,max=10, message='El campo debe tener entre 3 y 10 caracteres')
    ])
    nombre = StringField('Nombre', [
         validators.DataRequired(message='El campo es requerido')])
    apellido = StringField('Apellido', [
         validators.DataRequired(message='El campo es requerido')])
    email = EmailField('Correo',[
        validators.Email(message="Ingrese un correo valido")])