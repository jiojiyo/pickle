from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, TextAreaField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired,Length,EqualTo,Email
from wtforms.fields.html5 import EmailField

class UserCreateForm(FlaskForm):
    n_name = StringField('닉네임', validators=[DataRequired(), Length(min=2, max=10)])
    id = EmailField('이메일', validators=[DataRequired(), Email()])
    number = StringField('휴대폰 번호', validators=[DataRequired()])
    pw = PasswordField('비밀번호', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    id = EmailField('이메일', validators=[DataRequired("이메일을 입력해주세요")])
    pw = PasswordField('비밀번호', validators=[DataRequired("비밀번호를 입력해주세요")])

class FindIdForm(FlaskForm):
    number = StringField('휴대폰 번호', validators=[DataRequired("휴대폰번호를 입력해주세요")])

class FindPasswordForm(FlaskForm):
    id = EmailField('이메일', validators=[DataRequired(),Email()])
    number = StringField('휴대폰 번호', validators=[DataRequired()])

class UpdateInfo(FlaskForm):
    n_name = StringField('닉네임', validators=[DataRequired(),Length(min=2,max=10)])
    pw1 = PasswordField('비밀번호',validators=[DataRequired()])
    pw = PasswordField('초기 비밀번호', validators=[DataRequired()])

class PreferMovieForm(FlaskForm):
    mno = StringField('mmo')
    uno = StringField('uno')
    mpref = StringField('mpref')