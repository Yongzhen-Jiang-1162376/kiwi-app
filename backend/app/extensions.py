from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass

class Base(DeclarativeBase, MappedAsDataclass):
    pass

db = SQLAlchemy(model_class=Base)

from flask_migrate import Migrate
migrate = Migrate()

from flask_jwt_extended import JWTManager
jwt = JWTManager()
