from flask import Flask
from voice_api.blueprints.fs_api.views import fs_api
from voice_api.blueprints.web_api.views import web_api
from voice_api.models import db
from voice_api.models.ext_info import Ext_info

def creat_app():
    app=Flask(__name__)
    app.config.from_object('config')
    app.config.from_object('setting')
    app.register_blueprint(fs_api)
    app.register_blueprint(web_api)
    db.init_app(app)
    
    #创建数据库
    with app.app_context():
        db.create_all()

    return app