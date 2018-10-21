from flask import Flask
from flask_migrate import Migrate

def create_app(config):
    app = Flask(__name__)

    # Load global configuration
    app.config.from_object(config)

    # Init api and database
    from .model import db
    db.init_app(app)
    from .api import api
    api.init_app(app)

    migrate = Migrate(app, db)

    return app