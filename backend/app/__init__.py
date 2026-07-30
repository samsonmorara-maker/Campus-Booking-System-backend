"""
Initialize the Flask application.
"""

from flask import Flask

from app.config import Config
from app.extensions import db, migrate, jwt, cors

import app.models

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)
cors.init_app(app)

# Import routes
from app.routes import facilities