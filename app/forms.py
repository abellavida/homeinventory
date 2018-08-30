from flask import Flask, render_template, request, redirect, url_for, jsonify, flash # For flask implementation
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from wtforms.fields.html5 import DateField
from flask_wtf import FlaskForm
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5


class RegForm(FlaskForm):
    email = StringField('Email',  validators=[DataRequired(), Email(message='Invalid email'), Length(max=30)])
    username = StringField('Username',  validators=[DataRequired(), Length(min=3, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    password2 = PasswordField('Validate Password', validators=[DataRequired(), EqualTo('password'), Length(min=8, max=20)])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username',  validators=[DataRequired(), Length(min=3, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    submit = SubmitField('Submit')
    

class RecipeSearchForm(FlaskForm):
    protein = StringField('Main Ingredient', validators=[DataRequired()])
    vegetable = StringField('Vegetable')
    starch = StringField('Starch')
    genre = StringField('Type of dish (American, BBQ, Indian, Chinese, etc)')
    submit = SubmitField('Get Some Recipes')
    

class StorageLocationsForm(FlaskForm):
    location = StringField('Add a Food Storage (Pantry, Refrigerator, Garage Freezer, etc.)')
    submit = SubmitField('Submit')

class MealsForm(FlaskForm):
    breakfast = StringField('Breakfast')
    lunch = StringField('Lunch')
    dinner = StringField('Dinner')
    date = DateField('Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')



##class LoginForm(FlaskForm):
##    username = StringField('Username', validators=[DataRequired()])
##    password = PasswordField('Password', validators=[DataRequired()])
##    remember_me = BooleanField('Remember Me')
##    submit = SubmitField('Sign In')
##    
##class RegistrationForm(FlaskForm):
##	username = StringField('Username', validators=[DataRequired()])
##	email = StringField('Email', validators=[DataRequired(), Email()])
##	password = PasswordField('Password', validators=[DataRequired()])
##	password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
##	submit = SubmitField('Register')
##	
##	def validate_username(self, username):
##		user = User.query.filter_by(username=username.data).first()
##		if user is not None:
##			raise ValidationError('Please use a different username.')
##			
##	def validate_email(self, email):
##		user = User.query.filter_by(email=email.data).first()
##		if user is not None:
##			raise ValidationError('Please use a different email address.')
##			
##class EditProfileForm(FlaskForm):
##    username = StringField('Username', validators=[DataRequired()])
##    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
##    submit = SubmitField('Submit')
##
##    def __init__(self, original_username, *args, **kwargs):
##        super(EditProfileForm, self).__init__(*args, **kwargs)
##        self.original_username = original_username
##
##    def validate_username(self, username):
##        if username.data != self.original_username:
##            user = User.query.filter_by(username=self.username.data).first()
##            if user is not None:
##                raise ValidationError('Please use a different username.')
