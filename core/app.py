import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

config_obj = os.environ.get("CONFIG", "config.test")
app = Flask(__name__)
app.config.from_object(config_obj)
db = SQLAlchemy(app)

import api
