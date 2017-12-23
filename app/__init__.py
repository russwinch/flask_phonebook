from flask import Flask
import os

app = Flask(__name__, instance_relative_config=True)

from config import app_config
config_name = os.getenv('FLASK_CONFIG')
app.config.from_object(app_config[config_name])

from app import models
