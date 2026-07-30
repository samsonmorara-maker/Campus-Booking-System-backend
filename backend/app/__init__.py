from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt, cors, ma
import app.utils.jwt

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)
cors.init_app(app)
ma.init_app(app)

from app.routes import auth
from app.routes import users