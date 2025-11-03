from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from app.services.VacantesService import VacantesService

vacantes_bp = Blueprint('vacantes', __name__)

# crear vacante (post)
@vacantes_bp.route('/', methods=['POST'])
@jwt_required()
def crear_vacante():
    claims = get_jwt()
    if claims.get('rol') != 'Reclutador':
        return jsonify({"error": "Solo los reclutadores pueden crear vacantes"}), 403
    
    data = request.json
    nueva_vacante = VacantesService.crear_vacante(
        nombre_vacante=data.get('nombre'),
        descripcion_vacante=data.get('descripcion'),
        detalles_vacante=data.get('detalles'),
        estado_vacante='Disponible',
        id_reclutador=int(get_jwt_identity())
    )
    if nueva_vacante:
        return jsonify(nueva_vacante.to_dict()), 201
    return jsonify({"error": "No se pudo crear la vacante"}), 400

#editar vacantes (put)
@vacantes_bp.route('/<int:id_vacante>', methods=['PUT'])
@jwt_required()
def editar_vacante(id_vacante):
    claims = get_jwt()
    if claims.get('rol') != 'Reclutador':
        return jsonify({"error": "Solo los reclutadores pueden editar vacantes"}), 403
    
    # Verificar que sea el propietario
    if not VacantesService.verificar_propietario(id_vacante, int(get_jwt_identity())):
        return jsonify({"error": "No tienes permiso para editar esta vacante"}), 403
    
    data = request.json
    vacante_editada = VacantesService.editar_vacante(
        id_vacante=id_vacante,
        nombre_vacante=data.get('nombre'),
        descripcion_vacante=data.get('descripcion'),
        detalles_vacante=data.get('detalles')
    )
    if vacante_editada:
        return jsonify(vacante_editada.to_dict()), 200
    return jsonify({"error": "No se pudo editar la vacante"}), 400

#ver vacantes creadas (get)
@vacantes_bp.route('/mis-vacantes', methods=['GET'])
@jwt_required()
def ver_mis_vacantes():
    claims = get_jwt()
    if claims.get('rol') != 'Reclutador':
        return jsonify({"error": "Solo los reclutadores pueden ver sus vacantes"}), 403
    
    vacantes = VacantesService.listar_vacantes_por_reclutador(int(get_jwt_identity()))
    return jsonify([v.to_dict() for v in vacantes]), 200

#asignar postulante a vacante (put)
@vacantes_bp.route('/<int:id_vacante>/asignar', methods=['PUT'])
@jwt_required()
def asignar_postulante(id_vacante):
    claims = get_jwt()
    if claims.get('rol') != 'Reclutador':
        return jsonify({"error": "Solo los reclutadores pueden asignar postulantes"}), 403
    
    # Verificar que sea el propietario
    if not VacantesService.verificar_propietario(id_vacante, int(get_jwt_identity())):
        return jsonify({"error": "No tienes permiso para asignar postulantes a esta vacante"}), 403
    
    data = request.json
    vacante_asignada = VacantesService.asignar_postulante(
        id_vacante=id_vacante,
        id_postulante=data.get('id_postulante')
    )
    if vacante_asignada:
        return jsonify(vacante_asignada.to_dict()), 200
    return jsonify({"error": "No se pudo asignar el postulante"}), 400

# Para postulantes
# ver vacantes disponibles (get)
@vacantes_bp.route('/disponibles', methods=['GET'])
def ver_vacantes_disponibles():
    vacantes = VacantesService.obtener_vacantes_disponibles()
    return jsonify([v.to_dict() for v in vacantes]), 200

# ver ultimas tres vacantes
@vacantes_bp.route('/ultimas', methods=['GET'])
def ver_ultimas_tres_vacantes():
    vacantes = VacantesService.obtener_ultimas_tres_vacantes()
    return jsonify([v.to_dict() for v in vacantes]), 200

#ver detalles de la vacante (get)
@vacantes_bp.route('/<int:id_vacante>', methods=['GET'])
def ver_detalles_vacante(id_vacante):
    vacante = VacantesService.obtener_detalles_vacante(id_vacante)
    if vacante:
        return jsonify(vacante.to_dict()), 200
    return jsonify({"error": "Vacante no encontrada"}), 404
