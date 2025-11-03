from datetime import datetime
from app.models.VacanteModels import VacanteModel
from app.extensions import db

class VacantesService:
    @staticmethod
    def crear_vacante(nombre_vacante, descripcion_vacante, detalles_vacante, estado_vacante, id_reclutador):
        nueva_vacante = VacanteModel(
            nombre=nombre_vacante,
            descripcion=descripcion_vacante,
            detalles=detalles_vacante,
            fecha_publicacion=datetime.utcnow(),
            fecha_edicion=None,
            estado=estado_vacante,
            id_reclutador=id_reclutador
        )
        db.session.add(nueva_vacante)
        db.session.commit()
        return nueva_vacante
    
    @staticmethod
    def verificar_propietario(id_vacante, id_reclutador):
        vacante = VacanteModel.query.get(id_vacante)
        if not vacante:
            return False
        return vacante.id_reclutador == id_reclutador

    @staticmethod
    def editar_vacante(id_vacante, nombre_vacante, descripcion_vacante, detalles_vacante):
        vacante = VacanteModel.query.get(id_vacante)
        if not vacante:
            return None
        vacante.nombre = nombre_vacante
        vacante.descripcion = descripcion_vacante
        vacante.detalles = detalles_vacante
        vacante.fecha_edicion = datetime.utcnow()
        db.session.commit()
        return vacante

    @staticmethod
    def obtener_vacante_por_reclutador(id_vacante, id_reclutador):
        return VacanteModel.query.filter_by(id=id_vacante, id_reclutador=id_reclutador).first()
    
    @staticmethod
    def asignar_postulante(id_vacante, id_postulante):
        try:
            vacante = VacanteModel.query.filter_by(id=id_vacante, estado='Disponible').first()
            if not vacante:
                return None
            
            vacante.id_postulante = id_postulante
            vacante.estado = 'Ocupada'
            db.session.commit()
            return vacante
        except Exception as e:
            db.session.rollback()
            print(f"Error al asignar postulante: {e}")
            return None

    @staticmethod
    def obtener_vacantes_disponibles():
        try:
            return VacanteModel.query.filter_by(estado='Disponible').order_by(VacanteModel.fecha_publicacion.desc()).all()
        except Exception as e:
            print(f"Error al obtener vacantes disponibles: {e}")
            return []

    @staticmethod
    def obtener_ultimas_tres_vacantes():
        try:
            return VacanteModel.query.filter_by(estado='Disponible')\
                .order_by(VacanteModel.fecha_publicacion.desc())\
                .limit(3)\
                .all()
        except Exception as e:
            print(f"Error al obtener últimas vacantes: {e}")
            return []

    @staticmethod
    def obtener_detalles_vacante(id_vacante: int):
        try:
            return VacanteModel.query.get(id_vacante)
        except Exception as e:
            print(f"Error al obtener detalles de la vacante: {e}")
            return None

    @staticmethod
    def listar_vacantes_por_reclutador(id_reclutador):
        try:
            return VacanteModel.query.filter_by(id_reclutador=id_reclutador).all()
        except Exception as e:
            print(f"Error al obtener vacantes del reclutador: {e}")
            return []