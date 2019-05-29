from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired

class RegistrationForm(FlaskForm):
    name = StringField('Name: ',
                           validators=[DataRequired(), Length(min=2, max=20)])
    dob = DateTimeField('Date of birth: ')
    thana_code = StringField('Police station code: ',
                           validators=[DataRequired(), Length(min=2, max=20)])
    parent_name = StringField('Parent Name: ',
                           validators=[DataRequired(), Length(min=2, max=20)])
    contact_no = IntegerField('Contact Number:',
                           validators=[DataRequired()] )
    image_file = FileField('Image: ',
                           validators=[FileRequired(), FileAllowed(['jpg','png'], 'Images only!')])
    
    # submit = SubmitField('Register')