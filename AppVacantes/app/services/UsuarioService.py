from app.models.UsuarioModels import RolModel, UsuarioModel
from app.extensions import db


class UsuarioService:
    @staticmethod
    def obtenerUsuarios():
        usuarios = UsuarioModel.query.all()
        return usuarios

    @staticmethod
    def crearUsuario(nombre_usuario, password, rol_id):
        try:
            # Validar datos de entrada
            if not nombre_usuario or not password or not rol_id:
                return None, "Faltan datos obligatorios"

            # Verificar si el nombre de usuario ya existe
            if UsuarioModel.query.filter_by(nombre_usuario=nombre_usuario).first():
                return None, "El nombre de usuario ya existe"

            # Verificar si el rol existe
            if not RolModel.query.get(rol_id):
                return None, "El rol especificado no existe"

            usuario = UsuarioModel(
                nombre_usuario=nombre_usuario,
                password=password,
                rol_id=rol_id
            )

            # Guardar el nuevo usuario en la base de datos
            db.session.add(usuario)
            db.session.commit()

            return usuario, "Usuario creado exitosamente"
        except Exception as e:
            # En caso de error, revertir la transacción
            db.session.rollback()
            return None, f"Error al crear el usuario: {str(e)}"