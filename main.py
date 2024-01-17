from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()]) #DataRequired makes the two fields required fields
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


app = Flask(__name__)
app.secret_key = "thisisascretkey"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    form.validate_on_submit()
    print(form.email.data)
    print(form.password.data)
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
