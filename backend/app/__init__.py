"""Expose the Flask application for the Flask CLI."""

from app.app import app, create_app

__all__ = ["app", "create_app"]
