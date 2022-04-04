from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, FileField
from wtforms.validators import DataRequired 

class BookForm(FlaskForm):
    image = FileField('Book Image')
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    desc = StringField('Description', validators=[DataRequired()])
    price = DecimalField('Price', places=2, validators=[DataRequired()])
    submit = SubmitField('Add')
