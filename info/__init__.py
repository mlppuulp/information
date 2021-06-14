from flask import Flask
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis

from config import Config

app = Flask(__name__)

# 从类中加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)
# 设置redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启挡墙项目的保护,只做服务器的验证
CSRFProtect(app)
# 设置session保存指定位置(这句话必须设置,不让redis数据库中找不到添加的数据
Session(app)
