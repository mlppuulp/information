"""项目的入口启动文件"""
from flask.ext.wtf import CSRFProtect  # 服务器的请求保护
from redis import StrictRedis  # 指定redis的存储地址
from flask import Flask, session  # 使用session存储数据
from flask.ext.sqlalchemy import SQLAlchemy  # 数据库的配置
# 可以来指定session的保存位置
from flask_session import Session
from flask_script import Manager  # 使用命令行来控制程序的运行

app = Flask(__name__)


class Config(object):
    """项目的配置"""
    DEBUG = True

    SECRET_KEY = 'VoSiUUEOWfA6OxY1AlqtQnb2zpq0jr6NoAC7i42z2dGxyZ4SD/QTWTcSOZuHttL1'

    # 数据库的配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information13"
    # 不对数据库进行追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # session的配置
    SESSION_TYPE = "redis"
    # 是否对session开启签名(更加严密的保护)
    SESSION_USE_SIGNER = True
    # 是否永久保存session(默认session不过期,永久保存)
    SESSION_PERMANENT = False
    # 设置过期时间(时间为秒)
    PERMANENT_SESSION_LIFETIME = 86400 * 2
    # 指定session保存的redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


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

manager = Manager(app)


@app.route("/")
def index():
    session['name'] = "jiangguohe"
    session['age'] = 20

    return "ok"


if __name__ == '__main__':
    manager.run()
