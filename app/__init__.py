from flask import Flask
from config import Config
from app.extensions import db
from flask_migrate import Migrate

migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.main import bp as main_bp

    app.register_blueprint(main_bp)

    from app.user import bp as user_bp

    app.register_blueprint(user_bp, url_prefix="/user")
    
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix="/admin")



    return app
