""" Main entry file to the app"""

from flask import Flask
from config import Config
from app.extensions import db
from app.extensions import migrate
from app.extensions import bcrypt
from app.extensions import login_manager


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # Register blueprints
    from app.main.routes import  main
    from app.user.routes import user
    from app.admin.routes import admin

    app.register_blueprint(main)
    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(admin, url_prefix="/admin")

    return app

    
       


