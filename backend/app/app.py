"""
Flask application configuration.

Initializes extensions and registers routes.
"""

from flask import Flask

from app.config import Config
from app.extensions import db, migrate, jwt, cors

from app.routes.facilities import register_facility_routes

# Import models for SQLAlchemy
import app.models


def create_app():
    """
    Create and configure Flask application.
    """

    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    # Register routes
    register_facility_routes(app)

    return app