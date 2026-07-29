import os
from flask import Flask
from dotenv import load_dotenv
from app.extensions import db, migrate, jwt, cors

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)
cors.init_app(app)

from app.models import User, Facility, Booking

# Route modules registered here, at the bottom, AFTER app exists.
# Each import triggers that file's @app.route decorators to run.
# Uncomment each line once that teammate's file actually defines routes.
from app.routes import admin
# from app.routes import auth
# from app.routes import bookings
# from app.routes import facilities
# from app.routes import users
# from app.routes import schedules
# from app.routes import dashboard
