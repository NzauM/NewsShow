from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()


def create_app(config_name):


# Initializing application
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])


    bootstrap.init_app(app)
    #....
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)


# Flask extensions initialised by pasing app


# from app import views
# from app import error

    return app