
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
    app.register_blueprint(user_bp, url_prefix='/user')

    # with app.app_context():
    #     from app.models.user import User
    #     # Add other model imports here

    #     # Create the database tables
    #     db.create_all()

    return app
