from app.models.UsuarioModels import RolModel, UsuarioModel
from app.extensions import db


class UsuarioService:
    @staticmethod
    def obtener_usuarios():
        usuarios = UsuarioModel.query.all()
        return usuarios

    @staticmethod
    def crear_usuario(nombre_usuario, password, rol_id):
        try:
            # validar datos de entrada
            if not nombre_usuario or not password or not rol_id:
                return None, "Faltan datos obligatorios"

            # verificar si el nombre de usuario ya existe
            if UsuarioModel.query.filter_by(nombre=nombre_usuario).first():
                return None, "El nombre de usuario ya existe"

            # verificamos si el rol existe
            if not RolModel.query.get(rol_id):
                return None, "El rol especificado no existe"

            usuario = UsuarioModel(
                nombre=nombre_usuario,
                password=password,
                rol_id=rol_id
            )

            # Guardar el nuevo usuario en la base de datos
            db.session.add(usuario)
            db.session.commit()

            return usuario, "Usuario creado exitosamente"
        except Exception as e:
            db.session.rollback()
            return None, f"Error al crear el usuario: {str(e)}"

    @staticmethod
    def obtener_usuario_por_id(usuario_id):
        try:
            usuario = UsuarioModel.query.get(usuario_id)
            if not usuario:
                return None, "Usuario no encontrado"
            return usuario, None
        except Exception as e:
            return None, f"Error al buscar el usuario: {str(e)}"

    @staticmethod
    def actualizar_usuario(usuario_id, nombre=None, password=None, rol_id=None):
        try:
            usuario = UsuarioModel.query.get(usuario_id)
            if not usuario:
                return None, "Usuario no encontrado"

            # actualizar solo los campos proporcionados
            if nombre:
                # verificar si el nuevo nombre ya existe para otro usuario
                existe = UsuarioModel.query.filter(
                    UsuarioModel.nombre == nombre,
                    UsuarioModel.id != usuario_id
                ).first()
                if existe:
                    return None, "El nombre de usuario ya existe"
                usuario.nombre = nombre

            if password:
                usuario.password = password

            if rol_id:
                # verificar si el nuevo rol existe
                if not RolModel.query.get(rol_id):
                    return None, "El rol especificado no existe"
                usuario.rol_id = rol_id

            db.session.commit()
            return usuario, "Usuario actualizado exitosamente"
        except Exception as e:
            db.session.rollback()
            return None, f"Error al actualizar el usuario: {str(e)}"

    @staticmethod
    def eliminar_usuario(usuario_id):
        try:
            usuario = UsuarioModel.query.get(usuario_id)
            if not usuario:
                return False, "Usuario no encontrado"

            db.session.delete(usuario)
            db.session.commit()
            return True, "Usuario eliminado exitosamente"
        except Exception as e:
            db.session.rollback()
            return False, f"Error al eliminar el usuario: {str(e)}"