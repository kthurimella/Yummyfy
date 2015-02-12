# import the Flask class from the flask module
from flask import render_template, request, redirect, url_for

from questionnaire import Questionnaire
from forms import LoginForm
from app import app


questionnaire = Questionnaire("core")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/welcome', methods = ['POST', 'GET'])
def welcome():
    if request.method == 'POST':
        return redirect(url_for('menu'))
    # print questionnaire.get_assessment_results()
    else:
        return render_template('welcome.html')

@app.route('/assessment')
def assessment():
    questionnaire.create_new_questionnaire()
    return render_template('assessment.html', assessment_id = questionnaire.assessment.id)

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

@app.route('/recipe2')
def recipe2():
    return render_template('recipe2.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
