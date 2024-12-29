from flask import Flask
from config import Config
from app.extensions import db
import os
# from app.auth import auth
from app.bookmarks import bookmarks


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    if test_config:
        app.config.from_mapping(test_config)
    
    # Initialize Flask extensions here
    db.init_app(app)

    # register blueprints here
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp)
    
    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp)
    
    # app.register_blueprint(auth)
    app.register_blueprint(bookmarks)

    return app
