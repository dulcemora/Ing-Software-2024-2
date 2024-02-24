import pymysql
from datetime import datetime, timedelta

if __name__ == '__main__':
    try:
        connection = pymysql.connect(host='localhost',
                                 user='lab',
                                 password='Developer123!',
                                 db='lab_ing_software')
        print("Conexion correcta")
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error ", e)

#Funcion 1
def registraUsuario(nombre, password, email, profilePicture=None, superUser=False):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nombre, password, email, profilePicture, superUser) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, password, email, profilePicture, superUser))
        connection.commit()
    except pymysql.Error as e:
        print("Error ", e)
    finally:
        cursor.close()
def registraPelicula(nombre, genero, duracion, inventario):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)",
                       (nombre, genero, duracion, inventario))
        connection.commit()
    except pymysql.Error as e:
        print("Error ", e)
    finally:
        cursor.close()

def registraRenta(idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus=0):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)",
                       (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus))
        connection.commit()
    except pymysql.Error as e:
        print("Error ", e)
    finally:
        cursor.close()

#Funcion 2
def filtraUsuario(apellido):
    cursor = connection.cursor()

    try:
        consulta = "SELECT * FROM usuario WHERE apellido LIKE %s"
        apellido_param = f"%{apellido}"
        cursor.execute(consulta, (apellido_param,))

        resultados = cursor.fetchall()

        if resultados:
            print("Usuarios encontrados:")
            for usuario in resultados:
                print(usuario)
        else:
            print("No existen usuarios con ese apellido")

    except pymysql.Error as e:
        print("Error ", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#Funcion 3
def cambiaGeneroPelicula(nombre_pelicula, nuevo_genero):
    cursor = connection.cursor()
    try:
        consulta = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
        cursor.execute(consulta, (nuevo_genero, nombre_pelicula))

        if cursor.rowcount > 0:
            print("Se cambio el genero")
        else:
            print("No existe la pelicula")

        connection.commit()

    except pymysql.Error as e:
        print("Error ", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#Funcion 4
def eliminar_rentas_antiguas():
    cursor = connection.cursor()

    try:
        fecha_limite = datetime.now() - timedelta(days=3)

        consulta = "DELETE FROM rentas WHERE fecha_renta < %s"
        cursor.execute(consulta, (fecha_limite,))

        connection.commit()

        num_filas_afectadas = cursor.rowcount
        print(f"Se han eliminado {num_filas_afectadas} rentas antiguas.")

    except pymysql.Error as e:
        print("Error ", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()