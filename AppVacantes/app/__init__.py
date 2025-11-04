from flask import Flask
from dotenv import load_dotenv


from app.routes.usuarios_routes import usuarios_bp
from app.routes.roles_routes import roles_bp
from app.routes.vacantes_routes import vacantes_bp
from app.extensions import db, jwt
from config import Config
from app.models.UsuarioModels import UsuarioModel
from app.routes.auth_routes import auth_bp

load_dotenv()

# crear nuestra aplicacion
def create_app():
    app = Flask(__name__)
    # aceptar rutas con o sin barra final
    app.url_map.strict_slashes = False
    
    # cargar configuraciones
    app.config.from_object(Config)

    # inicializar extensiones
    db.init_app(app)
    # Inicializar JWTManager (necesario para crear/usar tokens JWT)
    jwt.init_app(app)
    
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
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(vacantes_bp, url_prefix='/vacantes')

    return app