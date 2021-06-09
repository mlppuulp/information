from redis import StrictRedis


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