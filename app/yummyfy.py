# import the Flask class from the flask module
from flask import render_template

from questionnaire import Questionnaire
from forms import LoginForm
from app import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/welcome')
def welcome():
  return render_template('welcome.html')

@app.route('/assessment')
def assessment():
    questionnaire = Questionnaire("core")
    questionnaire.create_new_questionnaire()
    return render_template('assessment.html', assessment_id = questionnaire.assessment.id)

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  return render_template('login.html', title='Sign In', form=form)