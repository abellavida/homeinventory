from flask import Flask
from flask_mongoengine import MongoEngine
from pymongo import MongoClient
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = "quenoledigaquenolecuenten"
##app.config['MONGODB_SETTINGS'] = {
##    'db' : 'carganwater',
##    'host' : 'mongodb://jcarter3:Carina1008!@ds249311.mlab.com:49311/carganwater',
##    'port' : 49311,
##    'username' : 'jcarter3',
##    'password' : 'Carina1008!'
##    }

app.config['MONGODB_SETTINGS'] = {
    'db' : 'temp'
    }
app.config['SOCIAL_FACEBOOK'] = {
    'consumer_key': '520051035121370',
    'consumer_secret': 'fc51c63a850d040ab1eedfe80a3d58ec'
}

client = MongoClient()
##client = MongoClient('ds249311.mlab.com', 49311)
##db = client['carganwater']
##db.authenticate('jcarter3','Carina1008!')

db = MongoEngine(app)

dbtemp = client.temp
dbhInv = client.homeinventory
