from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about yourslef.", validators=[Required()])  
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Leave your comment', validators=[Required()])
    submit = SubmitField("Comments")

class PostForm(FlaskForm):
    title = StringField("Title", validators=[Required()])
    description = TextAreaField("Wrie your blog..", validators=[Required()])
    submit = SubmitField("Submit Pitch")


