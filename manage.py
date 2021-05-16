"""项目的入口启动文件"""

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


# 从类中加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "index"


if __name__ == '__main__':
    app.run()
