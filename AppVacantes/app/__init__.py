from flask import Flask
from dotenv import load_dotenv


from app.routes.usuarios_routes import usuarios_bp
from app.routes.roles_routes import roles_bp
from app.extensions import db, jwt
from config import Config
from app.models.UsuarioModels import UsuarioModel

load_dotenv()

#crear nuestra aplicacion, devolver una instancia de la clase Flask con las configuraciones asignadas
def create_app():
    app = Flask(__name__)
    
    # Cargar configuraciones
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    
    with app.app_context():
        try:
            #db.drop_all()  # Eliminar las tablas existentes (si las hay)
            db.create_all()  # Crear las tablas en la base de datos si no existen
        except Exception as e:
            print(f"Error al crear las tablas: {e}")

    #cargar una configuracion
    app.config.from_object('config.Config')
    
    # Registrar blueprints
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
    app.register_blueprint(roles_bp, url_prefix='/roles')

    return app