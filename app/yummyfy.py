# import the Flask class from the flask module
from flask import render_template, redirect, url_for, request
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
    return render_template('assessment.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  return render_template('login.html', title='Sign In', form=form)