from database import db
from datetime import datetime


class Tarea(db.Model):
    __tablename__ = 'tareas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    estado = db.Column(db.String(20), nullable=False, default='pendiente')
    creada_en = db.Column(db.DateTime, default=datetime.utcnow)
    actualizada_en = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    ESTADOS_VALIDOS = ['pendiente', 'en_progreso', 'completada']

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'estado': self.estado,
            'creada_en': self.creada_en.strftime('%Y-%m-%d %H:%M:%S'),
            'actualizada_en': self.actualizada_en.strftime('%Y-%m-%d %H:%M:%S'),
        }
