from wtforms import Form, StringField, SubmitField, RadioField, IntegerField
from wtforms import validators


class ZodiacoForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido')
    ])
    apaterno = StringField('Apellido Paterno', [
        validators.DataRequired(message='El campo es requerido')
    ])
    amaterno = StringField('Apellido Materno', [
        validators.DataRequired(message='El campo es requerido')
    ])
    dia = IntegerField('Día', [
        validators.NumberRange(min=1, max=31, message='Día inválido')
    ])
    mes = IntegerField('Mes', [
        validators.NumberRange(min=1, max=12, message='Mes inválido')
    ])
    anio = IntegerField('Año', [
        validators.NumberRange(min=1500, max=2100, message='Año inválido')
    ])
    sexo = RadioField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M')
    enviar = SubmitField('Saber mi Signo')
