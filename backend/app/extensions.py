"""
app/extensions.py

This file creates shared Flask extension instances.

The extensions are created here without attaching them to the Flask app.
They will be initialized later inside create_app() using init_app().
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS


# SQLAlchemy instance
# Used to interact with the PostgreSQL database.
db = SQLAlchemy()


# Flask-Migrate instance
# Used to create and apply database migrations.
migrate = Migrate()


# JWT Manager instance
# Handles JSON Web Token authentication.
jwt = JWTManager()


# CORS instance
# Allows the React frontend to communicate with the Flask backend.
cors = CORS()