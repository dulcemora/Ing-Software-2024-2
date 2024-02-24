from sqlalchemy import Column, Integer, String, Boolean, LargeBinary

from alchemyClasses import db


class Usuario(db.Model):

    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    password = Column(String(64))
    email = Column(String(500), unique=True)
    profilePicture = Column(LargeBinary, nullable=True)
    superUser = Column(Boolean, nullable=True)

    def __init__(self, nombre, password, email, profilePicture=None, superUser=None):
        self.nombre = nombre
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser

    def __str__(self):
        return f'Nombre:{self.nombre}'