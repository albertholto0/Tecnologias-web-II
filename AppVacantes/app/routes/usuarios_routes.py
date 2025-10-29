from flask import Blueprint, request, jsonify
from app.services.UsuarioService import UsuarioService

# Se crea el Blueprint
usuarios_bp = Blueprint('usuarios', __name__)

# Listar usuarios
@usuarios_bp.route('/', methods=['GET'])
def obtener_todos():
    """Obtener todos los usuarios registrados"""
    usuarios = UsuarioService.obtener_usuarios()
    
    # Verificar si hay usuarios
    if not usuarios:
        return jsonify({'mensaje': 'No hay usuarios registrados'}), 404
    
    # Convertir usuarios a formato JSON
    usuarios_json = [{
        'id': u.id,
        'nombre': u.nombre,
        'rol_id': u.rol_id,
        'rol': u.rol.nombre_rol if u.rol else None
    } for u in usuarios]
    
    return jsonify(usuarios_json)

# Crear usuarios
@usuarios_bp.route('/', methods=['POST'])
def crear_usuario():
    """Crear un nuevo usuario"""
    datos = request.get_json() or {}
    
    # Validar campos requeridos
    if not datos.get('nombre') or not datos.get('password') or not datos.get('rol_id'):
        return jsonify({'error': 'Faltan campos obligatorios'}), 400
    
    # Llamar al servicio para crear el usuario
    usuario, mensaje = UsuarioService.crear_usuario(
        nombre_usuario=datos['nombre'],
        password=datos['password'],
        rol_id=datos['rol_id']
    )
    
    if not usuario:
        return jsonify({'error': mensaje}), 400
    
    # Convertir usuario a formato JSON
    usuario_json = {
        'id': usuario.id,
        'nombre': usuario.nombre,
        'rol_id': usuario.rol_id,
        'rol': usuario.rol.nombre_rol if usuario.rol else None
    }
    
    return jsonify({
        'mensaje': mensaje,
        'usuario': usuario_json
    }), 201

# Buscar un usuario por id
@usuarios_bp.route('/<int:usuario_id>', methods=['GET'])
def obtener_usuario_por_id(usuario_id):
    """Obtener un usuario por su ID"""
    usuario, mensaje = UsuarioService.obtener_usuario_por_id(usuario_id)
    
    if not usuario:
        return jsonify({'error': mensaje}), 404
    
    # Convertir usuario a formato JSON
    usuario_json = {
        'id': usuario.id,
        'nombre': usuario.nombre,
        'rol_id': usuario.rol_id,
        'rol': usuario.rol.nombre_rol if usuario.rol else None
    }
    
    return jsonify(usuario_json)

# Actualizar información de un usuario
@usuarios_bp.route('/<int:usuario_id>', methods=['PUT'])
def actualizar_usuario(usuario_id):
    """Actualizar la información de un usuario existente"""
    datos = request.get_json() or {}
    
    usuario, mensaje = UsuarioService.actualizar_usuario(
        usuario_id=usuario_id,
        nombre=datos.get('nombre'),
        password=datos.get('password'),
        rol_id=datos.get('rol_id')
    )
    
    if not usuario:
        return jsonify({'error': mensaje}), 400
    
    # Convertir usuario actualizado a formato JSON
    usuario_json = {
        'id': usuario.id,
        'nombre': usuario.nombre,
        'rol_id': usuario.rol_id,
        'rol': usuario.rol.nombre_rol if usuario.rol else None
    }
    
    return jsonify({
        'mensaje': mensaje,
        'usuario': usuario_json
    })

# Eliminar un usuario
@usuarios_bp.route('/<int:usuario_id>', methods=['DELETE'])
def eliminar_usuario(usuario_id):
    """Eliminar un usuario por su ID"""
    eliminado, mensaje = UsuarioService.eliminar_usuario(usuario_id)
    
    if not eliminado:
        return jsonify({'error': mensaje}), 404
        
    return jsonify({'mensaje': mensaje})