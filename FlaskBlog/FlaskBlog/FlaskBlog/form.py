from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from FlaskBlog.models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed 

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign up")
    def validate_username(self,username):
        user= User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError("That username is taken, Please choose another username")
        

    def validate_email(self,email):
        user= User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError("That email is taken, Please choose another email")

class SearchForm(FlaskForm):
    searched = StringField('Searched',validators=[DataRequired()])
    submit = SubmitField('Search')

class LoginForm(FlaskForm):
       
     email= StringField("Email",validators=[DataRequired(),Email()] )
     password= PasswordField("Password", validators=[DataRequired()])
     remember= BooleanField("Remember me")   
     submit= SubmitField("Log in")


class updateForm(FlaskForm):

    username= StringField("Username", validators=[DataRequired(),Length(min=2, max=20)])
    email= StringField("Email", validators=[DataRequired(),Email()])
    picture= FileField("Picture",validators=[FileAllowed(["jpg","png"])])
    submit= SubmitField("Update Profile")

    def validate_username(self,username):
            if current_user.username != username.data:
                user= User.query.filter_by(username=username.data).first()

                if user:
                    raise ValidationError("That username is taken, Please choose another username")
                

    def validate_email(self,email):
        if current_user.email != email.data:
            user= User.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError("That email is taken, Please choose another email")


class newPostForm(FlaskForm):
       
     title= StringField("Title",validators=[DataRequired()] )
     content= TextAreaField("Content",validators=[DataRequired()])
     submit= SubmitField("Post")
