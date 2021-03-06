from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, HiddenField
from wtforms import validators


class UserFormEdit(FlaskForm):
    user_name = StringField("Name: ", [validators.Length(2, 20, "Name should be from 2 to 20 symbols")])
    user_email = HiddenField("Email: ", [validators.Email("Wrong email format")])
    user_birthday = DateField("Birthday: ")
    user_phone = StringField("Phone: ", [validators.Length(20)])


    submit = SubmitField("Save")