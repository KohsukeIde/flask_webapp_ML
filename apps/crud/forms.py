from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, length


class UserForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username is required"),
            length(max=30, message="Username must be less than 30 characters"),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(message="Email is required"),
            Email(message="Email is invalid"),
        ],
    )
    password = PasswordField(
        "password",
        validators=[
            DataRequired(message="Password is required"),
        ],
    )
    submit = SubmitField("Submit")
