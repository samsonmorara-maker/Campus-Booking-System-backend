"""
Application entry point.

This file starts the Flask application.
It is also used by Flask CLI commands such as:

    flask run
    flask db migrate
    flask db upgrade
"""

from app.app import app

if __name__ == "__main__":
    app.run(debug=True)