from app.models.UsuarioModels import UsuarioModel

class AuthUsuario:
    @staticmethod
    def authenticateUser(nombre, password):
        usuario_db = UsuarioModel.query.filter_by(nombre=nombre).first()
        if usuario_db:
            if usuario_db.password == password:
                return usuario_db
        return None