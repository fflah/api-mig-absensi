from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_jwt_extended import JWTManager
from cryptography.fernet import Fernet

app = Flask(__name__, template_folder='views')
app.config.from_object(Config)
jwt = JWTManager(app)
api = Api(app, prefix='/api')
web = Api(app) 
db = SQLAlchemy(app)
migrate = Migrate(app, db)
key = b'53Birvb1KWD38mdVHBACHvbszJ6fslsXTzrsC_lhyjY='
fernet = Fernet(key)

from app import routes
from app.models import ModelActivity, ModelUser, ModelAbsensi