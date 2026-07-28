"""
app/config.py

Application configuration.

This file loads environment variables from the .env file
and provides configuration settings for the Flask app.
"""

import os

from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Config:
    """Base configuration for the Flask application."""

    # Secret key used by Flask
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Secret key used for JWT authentication
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    # PostgreSQL database connection
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # Disable modification tracking to improve performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False