
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from alchemyClasses import db

def query_all():
    return Usuario.query.all()

class Usuario(db.Model):

    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    apPat = Column(String(200))
    apMat = Column(String(200))
    password = Column(String(64))
    email = Column(String(500), unique=True)
    profilePicture = Column(LargeBinary, nullable=True)
    superUser = Column(Boolean, nullable=True)

    def __init__(self, nombre, apPat, apMat, password, email, profilePicture=None, superUser=None):
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser

    def __str__(self):
        return f'Nombre:{self.nombre}'


#def query():
#    return db.session.query(Usuario).all()