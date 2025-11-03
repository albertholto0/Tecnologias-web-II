from app.extensions import db

class VacanteModel(db.Model):
    __tablename__ = 'vacantes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'detalles': self.detalles,
            'fecha_publicacion': self.fecha_publicacion.isoformat() if self.fecha_publicacion else None,
            'fecha_edicion': self.fecha_edicion.isoformat() if self.fecha_edicion else None,
            'estado': self.estado,
            'id_reclutador': self.id_reclutador,
            'id_postulante': self.id_postulante
        }
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    detalles = db.Column(db.Text, nullable=True)
    fecha_publicacion = db.Column(db.DateTime, nullable=False)
    fecha_edicion = db.Column(db.DateTime, nullable=True)
    estado = db.Column(db.String(50), nullable=False)
    id_reclutador = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    id_postulante = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)