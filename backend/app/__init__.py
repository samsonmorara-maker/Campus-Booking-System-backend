"""
Expose Flask application factory.
"""

from app.app import create_app

__all__ = ["create_app"]