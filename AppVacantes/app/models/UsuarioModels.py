from app.extensions import db

class UsuarioModel(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255),nullable=False)
    
    # Relacion de tabla a rol
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    rol = db.relationship('RolModel', back_populates='usuarios')
    
class RolModel(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_rol = db.Column(db.String(100), nullable=False, unique=True)
    usuarios = db.relationship('UsuarioModel', cascade='all')
    
    
