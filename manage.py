"""项目的入口启动文件"""
# from flask.ext.wtf import CSRFProtect  # 服务器的请求保护
# from redis import StrictRedis  # 指定redis的存储地址
from flask import session  # 使用session存储数据
# from flask.ext.sqlalchemy import SQLAlchemy  # 数据库的配置
# 可以来指定session的保存位置
# from flask_session import Session
from flask_script import Manager  # 使用命令行来控制程序的运行
from flask_migrate import Migrate, MigrateCommand  # 数据库的迁移
# from config import Config
from info import app, db

manager = Manager(app)  # 生成迁移命令

# 将app 和 db 进行关联
Migrate(app, db)
# 加载迁移命令
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route("/")
def index():
    session['name'] = "jiangguohe"
    session['age'] = 20

    return "ok"


if __name__ == '__main__':
    manager.run()
