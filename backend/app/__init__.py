"""Initialize the Flask application and its extensions."""

from flask import Flask

from app.config import Config
from app.extensions import cors, db, jwt, ma, migrate
import app.models  # Ensure Flask-Migrate discovers every model.
import app.utils.jwt

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)
cors.init_app(
    app,
    resources={
        r"/api/*": {
            "origins": [
                "http://localhost:5173",
                
            ]
        }
    },
    methods=["GET", "POST","PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"]
)

ma.init_app(app)

# Import routes after the application and extensions are initialized.
from app.routes import admin, auth, bookings, facilities, schedules, users
