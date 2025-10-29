import os
from dotenv import load_dotenv

# Cargar .env aquí para que os.getenv() dentro de la clase Config vea las variables.
load_dotenv()


class Config:
    DEBUG = True  # Para que se recargue la app al guardar (ctrl + s).
    PORT = 5000  # Se puede cambiar el puerto.

    # Construir la URI con valores por defecto razonables
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '3306')
    DB_NAME = os.getenv('DB_NAME', 'vacantesdb')

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactivar para evitar warnings. Consume recursos.
    
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    JWT_ACCESS_TOKEN_EXPIRES = 86400  # Tiempo de expiración del token en segundos (24 horas)
    JWT_REFRESH_TOKEN_EXPIRES = 604800 # Tiempo de expiración del token de refresco en segundos (7 días)