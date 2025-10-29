from app.models.UsuarioModels import UsuariosModel
from flask import jsonify
from app.extensions import db

class RolService:

    @staticmethod
    def obtener_roles():
        roles = UsuariosModel.query.all()
        return roles
    
    @staticmethod
    def crear_rol(nombre_rol):

        if not nombre_rol:
            return jsonify({'error': 'Faltan campos obligatorios'}), 400
        
        if UsuariosModel.query.filter_by(nombre_rol=nombre_rol).first():
            return jsonify({'error': 'El nombre del rol ya existe'}), 400

        nuevo_rol = UsuariosModel(
            nombre_rol=nombre_rol
        )
        
        db.session.add(nuevo_rol)
        db.session.commit()
        return jsonify({'mensaje': 'Rol creado exitosamente', 'rol': nuevo_rol.to_dict()}), 201