from flask import Flask
from flask_mongoengine import Document
from config import app, db
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from flask_wtf import FlaskForm
from flask_login import UserMixin
from datetime import datetime
from mongoengine import *


class User(UserMixin, db.Document):
    meta = {'collection':'user'}
    email = db.StringField(max_length=30)
    username = db.StringField(max_length=30)
    password = db.StringField()
    social_id = db.StringField()

class RecipeSearch(Document):
    username = StringField()
    timestamp = db.ComplexDateTimeField()
    displayLink = db.StringField()
    link = db.URLField()
    htmlTitle = db.StringField()
    title = db.StringField()

class FoodStorages(Document):
    location = StringField()

class Meals(Document):
    breakfast = StringField()
    lunch = StringField()
    dinner = StringField()
    date = DateTimeField()


