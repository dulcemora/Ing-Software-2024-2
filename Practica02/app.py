from flask import Flask
from sqlalchemy import and_, or_

from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Rentar import Rentar
from cryptoUtils.CryptoUtils import cipher
from hashlib import sha256

#mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft
#<dialecto>+<driver>://<usuario>:<passwd>@localhost:3306/<db>
#mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_soft
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_soft'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        def salir():
            print("Saliendo")
            exit()

        def op1():
            print("Ver los registros de una tabla")
            print("Seleccione la tabla de la que desea ver los registros")

            while True:
                print("1. Tabla peliculas")
                print("2. Tabla usuarios")
                print("3. Tabla rentar")
                print("4. Salir")
                opp = input("Seleccione el numero que indica lo que desea hacer: ")

                if opp == "1":
                    print("Tabla peliculas")
                    for pelicula in Pelicula.query.all():  # Select * from pelicula
                        print(pelicula)
                elif opp == "2":
                    print("Tabla usuarios")
                    for usuario in Usuario.query.all():  # Select * from usuarios
                        print(usuario)
                elif opp == "3":
                    print("Tabla rentar")
                    for rentar in Rentar.query.all():  # Select * from rentar
                        print(rentar)
                elif opp == "4":
                    salir()
                else:
                    print("Opcion invalida. Vuelva a intentarlo.")


        def op2():
            print("Filtra los registros de una tabla por id")
            print("Seleccione la tabla de la que desea filtrar los registros")

            while True:
                print("1. Tabla peliculas")
                print("2. Tabla usuarios")
                print("3. Tabla rentar")
                print("4. Salir")
                opp2 = input("Seleccione el numero que indica lo que desea hacer: ")

                if opp2 == "1":
                    print("Tabla peliculas")
                    idPelicula = input("Ingrese el id: ")
                    aux = Pelicula.query.get(idPelicula)
                    print(aux)
                elif opp2 == "2":
                    print("Tabla usuarios")
                    idUsuario = input("Ingrese el id: ")
                    aux = Usuario.query.get(idUsuario)
                    print(aux)
                elif opp2 == "3":
                    print("Tabla rentar")
                    idRentar = input("Ingrese el id: ")
                    aux = Rentar.query.get(idRentar)
                    print(aux)
                elif opp2 == "4":
                    salir()
                else:
                    print("Opcion invalida. Vuelva a intentarlo.")


        def op3():
            print("Actualizar la columna de un registro(nombre para peliculas y usuarios, fecha para renta)")
            # nombre y para el caso Renta, modificar la fecha de la renta
            print("Seleccione la tabla de la que desea filtrar los registros")

            while True:
                print("1. Tabla peliculas")
                print("2. Tabla usuarios")
                print("3. Tabla rentar")
                print("4. Salir")
                opp3 = input("Seleccione el numero que indica lo que desea hacer: ")

                if opp3 == "1":
                    print("Tabla peliculas")
                    idPelicula = input("Ingrese el id: ")
                    if not idPelicula:
                        print("La pelicula no existe")
                    else:
                        nombre = input("Ingrese el nuevo nombre: ")
                        aux = Pelicula.query.get(idPelicula)
                        idPelicula.nombre = aux
                        db.session.commit()
                        print(aux)
                elif opp3 == "2":
                    print("Tabla usuarios")
                    idUsuario = input("Ingrese el id: ")
                    if not idUsuario:
                        print("El usuario no existe")
                    else:
                        nombre = input("Ingrese el nuevo nombre: ")
                        aux = Usuario.query.get(idUsuario)
                        idUsuario.nombre = aux
                        db.session.commit()
                        print(aux)
                elif opp3 == "3":
                    print("Tabla rentar")
                    idRentar = input("Ingrese el id: ")
                    if not idRentar:
                        print("La renta no existe")
                    else:
                        fecha = input("Ingrese la nueva fecha: ")
                        aux = Rentar.query.get(idRentar)
                        idRentar.fecha_renta = aux
                        db.session.commit()
                        print(aux)
                elif opp3 == "4":
                    salir()
                else:
                    print("Opcion invalida. Vuelva a intentarlo.")

        def op4():
            print("Eliminar un registro por id o todos los registros")


        while True:
            print("Menu:")
            print("1.Ver los registros de una tabla")
            print("2.Filtra los registros de una tabla por id")
            print("3. Actualizar la columna nombre de un registro")
            print("4. Eliminar un registro por id o todos los registros")
            print("5. Salir")
            op = input("Seleccione el numero que indica lo que desea hacer: ")

            if op == "1":
                op1()
            elif op == "2":
                op2()
            elif op == "3":
                op3()
            elif op == "4":
                op4()
            elif op == "5":
                salir()
            else:
                print("Opcion invalida. Vuelva a intentarlo.")