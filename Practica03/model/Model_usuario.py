from alchemyClasses.Usuario import Usuario
from alchemyClasses import db

def ver_usuario(id):
    return Usuario.query.filter_by(id=id).first()

def ver_usuarios():
    return Usuario.query.all()

def borra_usuario(idUsuario):
    usuario = Usuario.query.filter(Usuario.idUsuario).first()
    db.session.delete(usuario)
    db.session.commit()