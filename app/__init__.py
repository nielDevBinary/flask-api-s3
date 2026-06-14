from flask import Flask
from .config import Config
from .extensions import db, migrate
from .routes.user_routes import user_bp
from .routes.file_routes import file_bp

from .core.error_handler import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(file_bp, url_prefix="/api/files")


    # Manejo global de errores
    register_error_handlers(app)

    return app     