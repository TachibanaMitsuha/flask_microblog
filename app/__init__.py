from logging.handlers import RotatingFileHandler, SMTPHandler
import os
import logging

from flask import Flask
from flask_mail import Mail

from config import Config
from flask_sqlalchemy import SQLAlchemy#从包中导入类
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
#print('等会谁（哪个包或模块）在使用我:{}'.format(__name__))
#print(app.config['SECRET_KEY'])

db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象

login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)

from app import routes,models,errors

if not app.debug:
    #if not os.path.exists('logs'):
    #     os.mkdir('logs')
    # file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
    #                                    backupCount=10)
    # file_handler.setFormatter(logging.Formatter(
    #     '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    # file_handler.setLevel(logging.INFO)
    # app.logger.addHandler(file_handler)
    #
    # app.logger.setLevel(logging.INFO)
    # app.logger.info('Microblog startup')

    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
