from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

"""
Aqui se inicializan las extensiones que se usaran en la aplciación
"""