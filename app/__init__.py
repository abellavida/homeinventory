from flask import Flask
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from datetime import datetime
from config import app


login = LoginManager(app)
login.login_view = 'login'
