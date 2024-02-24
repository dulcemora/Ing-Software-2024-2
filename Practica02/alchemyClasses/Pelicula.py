from sqlalchemy import Column, Integer, String

from alchemyClasses import db


class Pelicula(db.Model):

    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    genero = Column(String(45), nullable=True)
    duracion = Column(Integer, nullable=True)
    inventario = Column(Integer)

    def __init__(self, nombre, inventario, genero=None, duracion=None):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f'Nombre:{self.nombre}'