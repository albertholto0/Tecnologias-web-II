from flask import Blueprint, request, jsonify
from app.models.UsuarioModels import UsuarioModel
from app.services.AuthUsuario import AuthUsuario
from flask_jwt_extended import create_access_token, create_refresh_token

auth_bp = Blueprint('roles', __name__)

@auth_bp.route('/login', methods=['POST'])

def login():
    data = request.get_json()
    usuario = UsuarioModel(
        nombre = data.get('nombre'),
        password = data.get('password')
    )
    
    auth_usuario = AuthUsuario.authenticateUser(
        nombre=usuario.nombre,
        password=usuario.password
    )
    
    if auth_usuario:
        nombre_rol = auth_usuario.rol.nombre_rol
        access_token = create_access_token(
            identity=str(auth_usuario.id),
            # opcionarl pero necesario para el control de roles
            additional_claims={
                'rol': nombre_rol
            }
        )
        # esto es para refrescar el token
        refresh_token = create_refresh_token(
            identity=str(auth_usuario.id)
        )
        
        return jsonify({
            'mensaje': 'Inicio de sesión exitoso',
            'data': {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'usuario': {
                    'id': auth_usuario.id,
                    'nombre_usuario': auth_usuario.nombre_usuario,
                    'rol': nombre_rol
                }
            }
        }), 200