from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt, cors, ma

main = Flask(__name__)

main.config.from_object(Config)

db.init_app(main)
migrate.init_app(main, db)
jwt.init_app(main)
cors.init_app(main)
ma.init_app(main)

# Import routes after creating the app
import app.routes.auth
import app.routes.users