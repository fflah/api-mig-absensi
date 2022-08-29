import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    SECRET_KEY = str(os.environ.get("SECRET_KEY"))
    SQLALCHEMY_DATABASE_URI = 'postgresql://colafzxcwiluva:f7cdeecdd88c685f7930006a3432211bd0aafc92dcadbf4157f7a71b490b6da5@ec2-34-234-240-121.compute-1.amazonaws.com:5432/d14cs2dvisad07'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    JWT_ALGORITHM = str(os.environ.get("JWT_ALGORITHM"))