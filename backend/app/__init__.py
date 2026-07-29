from flask import Flask

from app.config import Config
from app.extensions import db, migrate, ma


app = Flask(__name__)

app.config.from_object(Config)


db.init_app(app)
migrate.init_app(app, db)
ma.init_app(app)


# Import routes so Flask registers them
from app.routes import bookings
from app.routes import schedules