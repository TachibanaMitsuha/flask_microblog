from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy#从包中导入类
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
#print('等会谁（哪个包或模块）在使用我:{}'.format(__name__))
#print(app.config['SECRET_KEY'])

db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象

from app import route,models