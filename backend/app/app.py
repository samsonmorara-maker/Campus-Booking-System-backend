"""
Flask application configuration.

Initializes extensions and registers routes.
"""

from flask import Flask

from app.config import Config
from app.extensions import db, migrate, jwt, cors

from app.routes.facilities import (
    get_facilities,
    get_single_facility,
    search,
    add_facility,
    edit_facility,
    remove_facility,
)

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


    return app


app = create_app()


# ----------------------------
# Facility Routes
# ----------------------------

app.add_url_rule(
    "/api/facilities",
    view_func=get_facilities,
    methods=["GET"]
)

app.add_url_rule(
    "/api/facilities/<int:facility_id>",
    view_func=get_single_facility,
    methods=["GET"]
)

app.add_url_rule(
    "/api/facilities/search",
    view_func=search,
    methods=["GET"]
)

app.add_url_rule(
    "/api/facilities",
    view_func=add_facility,
    methods=["POST"]
)

app.add_url_rule(
    "/api/facilities/<int:facility_id>",
    view_func=edit_facility,
    methods=["PUT"]
)

app.add_url_rule(
    "/api/facilities/<int:facility_id>",
    view_func=remove_facility,
    methods=["DELETE"]
)