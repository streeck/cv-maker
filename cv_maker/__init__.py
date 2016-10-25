from flask import Flask
from flask_bootstrap import Bootstrap

from .cv_maker import cv_maker
from .nav import nav


def create_app(configfile=None):
    app = Flask(__name__)

    Bootstrap(app)

    app.register_blueprint(cv_maker)

    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.config['SECRET_KEY'] = 'supersekret'

    nav.init_app(app)

    return app
