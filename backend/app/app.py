"""
app/app.py

Main Flask application file.

This file creates the Flask application,
loads configuration, initializes extensions,
and prepares the backend.
"""

from flask import Flask

from app.config import Config
from app.extensions import (
    cors,
    db,
    jwt,
    migrate,
)

from app.routes.facilities import (
    register_facility_routes,
)

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

    # Initialize database
    db.init_app(app)

    # Initialize migrations
    migrate.init_app(app, db)

    # Initialize JWT
    jwt.init_app(app)

    # Enable CORS
    cors.init_app(app)

    # Register facility routes
    register_facility_routes(app)

    return app


# Create application instance
app = create_app()