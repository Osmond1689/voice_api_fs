from flask import Flask
from voice_api.blueprints.fs_api.views import fs_api
from voice_api.blueprints.web_api.views import web_api
from voice_api.models import db
import logging
from logging.handlers import TimedRotatingFileHandler

def creat_app():
    app=Flask(__name__)
    app.config.from_object('config')
    app.config.from_object('setting')
    app.register_blueprint(fs_api)
    app.register_blueprint(web_api)
    #日志
    # 设置最开始的日志级别
    logging.basicConfig(level=logging.DEBUG)
    formatter = logging.Formatter(
        "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
    handler = TimedRotatingFileHandler(
        "voice.log", when="D", interval=1, backupCount=7,
        encoding="UTF-8", delay=False, utc=True)
    app.logger.addHandler(handler)
    handler.setFormatter(formatter)

    db.init_app(app)
    
    #创建数据库
    with app.app_context():
        db.create_all()

    return app