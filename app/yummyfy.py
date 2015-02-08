# import the Flask class from the flask module
from flask import render_template, redirect, url_for, request
from app import app


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/welcome')
def welcome():
  return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  return render_template('login.html', title='Sign In', form=form)