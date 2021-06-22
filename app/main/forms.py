from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about yourslef.", validators=[Required()])  
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Leave your comment', validators=[Required()])
    submit = SubmitField("Comment")

class PostForm(FlaskForm):
    title = StringField("Title", validators=[Required()])
    content = TextAreaField("Wrie your blog..", validators=[Required()])
    submit = SubmitField("Submit Pitch")

class SubscriptionForm(FlaskForm):
    email= StringField("Enter a valid email address", validators=[Required()])
    submit = SubmitField('Subscribe')


