"""项目的入口启动文件"""
from flask.ext.wtf import CSRFProtect  # 服务器的请求保护
from redis import StrictRedis  # 指定redis的存储地址
from flask import Flask, session  # 使用session存储数据
from flask.ext.sqlalchemy import SQLAlchemy  # 数据库的配置
# 可以来指定session的保存位置
from flask_session import Session
from flask_script import Manager  # 使用命令行来控制程序的运行
from flask_migrate import Migrate,MigrateCommand  # 数据库的迁移
from config import Config

app = Flask(__name__)

# 从类中加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)

manager = Manager(app)  # 生成迁移命令

# 将app 和 db 进行关联
Migrate(app,db)
# 加载迁移命令
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


# 设置redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启挡墙项目的保护,只做服务器的验证
CSRFProtect(app)
# 设置session保存指定位置(这句话必须设置,不让redis数据库中找不到添加的数据
Session(app)


@app.route("/")
def index():
    session['name'] = "jiangguohe"
    session['age'] = 20

    return "ok"


if __name__ == '__main__':
    manager.run()
