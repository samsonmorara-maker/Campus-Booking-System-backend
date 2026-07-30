"""
Main application entry point.

Runs the Flask server.
"""

from app import app


if __name__ == "__main__":
    app.run(debug=True)