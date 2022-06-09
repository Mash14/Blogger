from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired


# An example
class UpdateProfileForm(FlaskForm):
    bio = StringField('Update Bio')
    submit = SubmitField('Post')

class CreateBlogForm(FlaskForm):
    title = StringField('Title',validators=[InputRequired()])
    post = TextAreaField('Blog')
    category = SelectField('Blog Category',choices=[('Food','Food'),('People','People'),('Jobs','Jobs'),('Internet','Internet'),('Massage','Massage'),('Revolution','Revolution'),('Idea','Idea'),('Music','Music'),('Drip','Drip')],validators=[InputRequired()])
    submit = SubmitField('Post')

class CreateCommentForm(FlaskForm):
    comment = TextAreaField('Comment')
    submit = SubmitField('Post')