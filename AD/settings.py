# -*- coding: utf-8 -*-


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "110affdfghrwwqcbnyy"
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'redis'
    CACHE_DEFAULT_TIMEOUT = 60 * 2


def get_db_uri(dbinfo):
    user = dbinfo.get("USER") or "ad_user"
    password = dbinfo.get("PASSWORD") or "ad_pass"
    host = dbinfo.get("HOST") or "127.0.0.1"
    port = dbinfo.get("PORT") or "3306"
    name = dbinfo.get("NAME") or "mysql"
    db = dbinfo.get("DB") or "ad"
    driver = dbinfo.get("driver") or "pymysql"

    return "{}+{}://{}:{}@{}:{}/{}".format(db, driver, user, password, host, port, name)


class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        "USER": 'ad_user',
        "PASSWORD": 'Ycxx123#',
        'HOST': '192.168.170.142',
        'PORT': '3306',
        'NAME': 'ad_flask',
        "DB": "mysql",
        "driver": "pymysql"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = True

    DATABASE = {
        "USER": 'ad_user',
        "PASSWORD": 'ad_pass',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'ad',
        "DB": "mysql",
        "driver": "pymysql"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DEBUG = True

    DATABASE = {
        "USER": 'ad_user',
        "PASSWORD": 'ad_pass',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'ad',
        "DB": "mysql",
        "driver": "pymysql"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


config = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
