"""
Main application entry point.

Runs the Flask server.
"""

from app.app import app


if __name__ == "__main__":
    app.run(debug=True)