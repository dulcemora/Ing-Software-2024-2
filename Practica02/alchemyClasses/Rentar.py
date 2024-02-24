from alchemyClasses import db
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from datetime import date

class Rentar(db.Model):

    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuario.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('pelicula.idPelicula'))
    fecha_renta = Column(DateTime)
    dias_de_renta = Column(Integer, nullable=True)
    estatus = Column(Boolean, nullable=True)

    def __init__(self, idUsuario, idPelicula, fecha_renta=date.today(), dias_de_renta=None, estatus=None):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        return f"Usuario: {self.idUsuario}\nRentar: {self.idRentar}\nFecha: {self.fecha_renta}"