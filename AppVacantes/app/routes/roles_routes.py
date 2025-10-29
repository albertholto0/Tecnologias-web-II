from flask import Blueprint, request, jsonify
from app.services.RolService import RolService

roles_bp = Blueprint('roles', __name__)

# Obtener todos los roles
@roles_bp.route('/', methods=['GET'])
def obtener_roles():
    roles = RolService.obtener_roles()

    # Convertir los datos a un JSON
    roles_json = [{
        'id': rol.id,
        'nombre_rol': rol.nombre_rol,
        'usuarios': [u.nombre for u in rol.usuarios] 
    } for rol in roles]
    
    return jsonify(roles_json), 200

# Crear un nuevo rol
@roles_bp.route('/crear', methods=['POST'])
def crear_rol():
    try:
        datos = request.get_json(force=True) or {}
    except Exception as e:
        return jsonify({'error': 'El body debe ser un JSON válido'}), 400
        
    if not datos.get('nombre_rol'):
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    rol, mensaje = RolService.crear_rol(datos['nombre_rol'])
    
    if not rol:
        return jsonify({'error': mensaje}), 400

    return jsonify({
        'mensaje': mensaje,
        'rol': {
            'id': rol.id,
            'nombre_rol': rol.nombre_rol
        }
    }), 201