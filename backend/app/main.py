from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt, cors, ma

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)
cors.init_app(app)
ma.init_app(app)

from app.routes.auth import register_auth_routes
from app.routes.users import register_user_routes

register_auth_routes(app)
register_user_routes(app)