from flask import Flask

from flaskdemo import settings
from flaskdemo.extension import init_extension
from api.player_api import blue


def create_app(env_name):
    app = Flask(__name__)
    app.register_blueprint(blue)
    app.config.from_object(settings.config.get(env_name) or 'default')
    init_extension(app=app)
    return app