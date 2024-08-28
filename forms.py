from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class MarcaForm(FlaskForm):
    # name = StringField('nombre', validators=[DataRequired()])
    name = StringField('Nombre')
    submit = SubmitField('Guardar')
