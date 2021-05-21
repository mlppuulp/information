"""项目的入口启动文件"""
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    """项目的配置"""
    DEBUG = True
    # 数据库的配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information13"
    # 不对数据库进行追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

# 从类中加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)

# 设置redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)

# 开启挡墙项目的保护,只做服务器的验证
CSRFProtect(app)

@app.route("/")
def index():
    return "index"


if __name__ == '__main__':
    app.run()
