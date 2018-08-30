from config import db, dbtemp, dbhInv, app
import json
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash # For flask implementation
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import flask_excel as excel
from forms import RecipeSearchForm, RegForm, LoginForm, StorageLocationsForm, MealsForm
from models import User, RecipeSearch, FoodStorages, Meals
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from recipe_search import recipe_search
##import pymongo

def dateconverter(d):
    if isinstance(d, datetime):
        return "{}-{}-{}".format(d.year, d.month, d.day)

title = "Home Meal Planning"
heading = "Home Meal Planning"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if request.method == 'POST':
        if form.validate():
            existing_user = User.objects(email=form.email.data).first()
            if existing_user is None:
                hashpass = generate_password_hash(form.password.data, method='sha256')
                hey = User(form.email.data,form.username.data,hashpass).save()
                login_user(hey)
                return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == True:
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            check_user = User.objects(username=form.username.data).first()
            if check_user:
                if check_password_hash(check_user['password'], form.password.data):
                    login_user(check_user)
                    return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/recipesearch', methods=['GET', 'POST'])
@login_required
def recipesearch():
    form = RecipeSearchForm()
    terms = ('recipe %s %s %s %s' %(form.protein.data, form.vegetable.data, form.starch.data, form.genre.data))
    username = 'jenn'
    if request.method == 'POST':
        recipe_search(username, terms)
        return redirect(url_for('recipesearchresults'))
    return render_template('recipesearch.html', form=form)


@app.route('/recipesearchresults', methods=['GET', 'POST'])
@login_required
def recipesearchresults():
    results = dbtemp.recipe_search.find()
    return render_template("recipesearchresults.html", title='Recipe Search Results', results=results)

@app.route('/foodstorages', methods=['GET','POST'])
@login_required
def foodstorages():
    foodstorages = StorageLocationsForm()
    if request.method == 'POST':
        try:
            if dbtemp.foodstorages.get(foodstorages.data):
                pass
            else:
                dbtemp.foodstorages.save(foodstorages.data)
        except:
            pass
    storages = dbtemp.foodstorages.find()
    return render_template('foodstorages.html', title='Food Storage Locations', storages=storages, foodstorages=foodstorages)

@app.route('/planmeals', methods=['GET','POST'])
@login_required
def planmeals():
    meals = Meals()
    mealplan = dbtemp.meals.find()
    mealform = MealsForm()
    if request.method == 'POST':
        meals.date = mealform.date.data
        meals.breakfast = mealform.breakfast.data
        meals.lunch = mealform.lunch.data
        meals.dinner = mealform.dinner.data
        try:
            if meals.date == dbtemp.meals.get(mealform.date.data):
                meals.update()
            else:
                meals.save()
        except:
            pass
    
    return render_template('planmeals.html', title='Meal Planning', mealform = mealform, mealplan = mealplan)


@app.route('/mealplan.json')
def mealplanjson():
    mealplan = Meals.objects()
    json_data = mealplan.to_json()
    return json.dumps(json_data)

@app.route('/logout', methods = ['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
##    app.run(debug=True)
