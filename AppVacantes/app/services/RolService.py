from app.models.UsuarioModels import RolModel
from app.extensions import db

class RolService:
    @staticmethod
    def obtener_roles():
        roles = RolModel.query.all()
        return roles

    @staticmethod
    def crear_rol(nombre_rol):
        try:
            # Validar datos de entrada
            if not nombre_rol:
                return None, "Falta el nombre del rol"

            # Verificar si el rol ya existe
            if RolModel.query.filter_by(nombre_rol=nombre_rol).first():
                return None, "El nombre del rol ya existe"

            nuevo_rol = RolModel(
                nombre_rol=nombre_rol
            )

            # Guardar el nuevo rol en la base de datos
            db.session.add(nuevo_rol)
            db.session.commit()

            return nuevo_rol, "Rol creado exitosamente"
        except Exception as e:
            # En caso de error, revertir la transacción
            db.session.rollback()
            return None, f"Error al crear el rol: {str(e)}"