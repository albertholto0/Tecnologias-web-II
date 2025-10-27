from flask import Flask
from dotenv import load_dotenv
from app.routes.UsuariosRoutes import usuarios_bp
from app.extensions import db, jwt
from config import Config

load_dotenv()

#crear nuestra aplicacion, devolver una instancia de la clase Flask con las configuraciones asignadas
def create_app():
    app = Flask(__name__)
    
    # Cargar configuraciones
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    
    with app.app_context():
        #db.drop_all()  # Eliminar las tablas existentes (si las hay)
        db.create_all()  # Crear las tablas en la base de datos si no existen

    #cargar una configuracion
    app.config.from_object('config.Config')

    app.register_blueprint(usuarios_bp,urlprefix='/usuarios')

    return app