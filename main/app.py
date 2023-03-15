from flask import Flask
from flask_jwt_extended import JWTManager


from main.extensions import db, migrate, cors
from main.settings import DevSettings

from main.modules import user, product, receipt

MODULES = [user, product, receipt]


def create_app(settings=DevSettings):
    app = Flask(__name__)

    # Setup the Flask-JWT-Extended extension

    app.config.from_object(settings)
    app.config["JWT_SECRET_KEY"] = "HBDZ"

    jwt = JWTManager(app)

    # Utiliser la configuration (settings).

    # Init SQLAlchemy
    db.init_app(app)
    cors.init_app(app)

    # Init Migrate
    migrate.init_app(app, db)
    register_modules(app)
    register_shell_context(app)

    return app


def register_shell_context(app):
    def shell_context():
        return{'db': db}
    app.shell_context_processor(shell_context)


def register_modules(app):
    for m in MODULES:
        if hasattr(m, 'api'):
            app.register_blueprint(m.api)
