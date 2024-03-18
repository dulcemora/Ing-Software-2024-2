from alchemyClasses.Pelicula import Pelicula
from alchemyClasses import db

def ver_pelicula(id):
    return Pelicula.query.filter_by(id=id).first()

def ver_peliculas():
    return Pelicula.query.all()

def borra_pelicula(idPelicula):
    pelicula = Pelicula.query.filter(Pelicula.idPelicula).first()
    db.session.delete(pelicula)
    db.session.commit()