"""
app/app.py

Main Flask application file.

This file creates the Flask application,
loads configuration, initializes extensions,
and prepares the backend.
"""

from flask import Flask

from app.config import Config
from app.extensions import cors, db, jwt, migrate
from app.routes.facilities import facility_bp

# Import all models so Flask-Migrate can detect them
import app.models


def create_app():
    """
    Application factory function.

    Creates and configures the Flask application.
    """

    app = Flask(__name__)

    # Load configuration settings
    app.config.from_object(Config)

    # Initialize Flask extensions

    # Connect database to Flask app
    db.init_app(app)

    # Connect migration system
    migrate.init_app(app, db)

    # Connect JWT authentication
    jwt.init_app(app)

    # Allow React frontend communication
    cors.init_app(app)
    app.register_blueprint(facility_bp)

    return app


# Create application instance
app = create_app()