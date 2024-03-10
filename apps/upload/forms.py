from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField

class UploadForm(FlaskForm):
    file = FileField('File', validators=[FileAllowed(['jpg', 'png', 'gif', 'pdf'], 'Images and PDFs only!')])
    submit = SubmitField('Upload')