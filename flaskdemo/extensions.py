from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_restful import Api
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
debugtoolbar = DebugToolbarExtension()
cache = Cache(config={
    "CACHE_TYPE": 'redis',
    "CACHE_KEY_PREFIX": 'AD_',
    "ACHE_DEFAULT_TIMEOUT": 60 * 2,
    #TODO:和别的使用redis的服务分开数据库,使用密码
    # "CACHE_REDIS_URL": 'redis://user:password@localhost:6379/2',
})
api = Api()

def init_extension(app):
    db.init_app(app)
    Session(app)
    migrate.init_app(app, db=db)
    debugtoolbar.init_app(app)
    cache.init_app(app)
    api.init_app(app)

