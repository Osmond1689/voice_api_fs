from flask import Flask
from voice_api.blueprints.fs_api import fs_api
from voice_api.blueprints.web_api import web_api

def creat_app():
    app=Flask(__name__)
    app.config.from_object('config')
    app.config.from_object('setting')
    app.register_blueprint(fs_api)
    app.register_blueprint(web_api)
    return app