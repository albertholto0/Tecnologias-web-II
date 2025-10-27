from flask import Blueprint, jsonify, request
from app.services.UsuarioService import UsuarioService

# Establecer planos para estas rutas
usuarios_bp = Blueprint('usuarios', __name__)

# Listar usuarios
@usuarios_bp.route('/', methods=['GET'])
def obtener_todos():
    usuarios = UsuarioService.obtenerUsuarios()

    if not usuarios:
        return jsonify({"message": "No hay usuarios en la base de datos"}), 404

    return jsonify(usuarios), 200

# Crear usuarios
@usuarios_bp.route('/', methods=['POST'])
def crear_usuario():
    try:
        data = request.get_json()
        nombre_usuario = data.get('nombre_usuario')
        password = data.get('password')
        rol_id = data.get('rol_id')

        usuario, mensaje = UsuarioService.crearUsuario(nombre_usuario, password, rol_id)

        if usuario is None:
            return jsonify({"error": mensaje}), 400

        data = {"mensaje": mensaje,
                "usuario": {
                    "id": usuario.id,
                    "nombre_usuario": usuario.nombre_usuario,
                    "rol_id": usuario.rol_id
                }}

        return jsonify(data), 201

    except Exception as e:
        return jsonify({"error": "Error al crear el usuario", "detalle": str(e)}), 500

#Correr la aplicacion 
#probar los endpoints en postman
#Buscar un usuario por id
@usuarios_bp.route('/<int:usuario_id>', methods=['GET'])
def obtener_usuario_por_id(usuario_id):
    usuario = UsuarioService.obtenerUsuarioPorId(usuario_id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario), 200

#Buscar un usuario por id (mockup sin base de datos)
def obtener_usuario_por_id(usuario_id):
    for usuario in usuarios:
        if usuario.get('id') == usuario_id:
            return jsonify(usuario), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404

#Actualizar informacion de usuario
@usuarios_bp.route('/', methods=['PUT'])
def actualizar_usuario(usuario_id):
    datos_actualizados = request.get_json()
    for usuario in usuarios:
        if usuario.get('id') == usuario_id:
            usuario.update(datos_actualizados)
            return jsonify({'mensaje': 'Usuario actualizado', 'usuario': usuario}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404


