from flask import Blueprint, request, render_template, flash, redirect, url_for
from alchemyClasses.Pelicula import Pelicula, db
#from model.Model_pelicula import borra_pelicula
from sqlalchemy.exc import IntegrityError

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/', methods=['GET'])
def raizpelicula():
    return render_template('Pelicula/raizpelicula.html')

@pelicula_blueprint.route('/ver_peliculas', methods=['GET'])
def ver_peliculas():
    peliculas = Pelicula.query.all()

    for pelicula in peliculas:
        print(f"ID: {pelicula.idPelicula}, Nombre: {pelicula.nombre}, Genero: {pelicula.genero}")
    return render_template('Pelicula/ver_peliculas.html', peliculas=peliculas)

@pelicula_blueprint.route('/agregar_pelicula', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'POST':
        nombr = request.form['nombre']
        gen = request.form['genero']
        dur = request.form['duracion']
        inv = request.form['inventario']

        nueva_pelicula = Pelicula(nombre=nombr, genero=gen, duracion=dur, inventario=inv)
        try:
            db.session.add(nueva_pelicula)
            db.session.commit()
            flash('Pelicula agregada correctamente', 'success')
            return redirect(url_for('pelicula.agregar_pelicula'))
        except IntegrityError:
            db.session.rollback()  # Revertir los cambios realizados en la transacción
#            flash('Error: El correo electrónico ya está registrado', 'error')
            return redirect(url_for('pelicula.agregar_pelicula'))

    return render_template('Pelicula/agregar_pelicula.html')



@pelicula_blueprint.route('/borrar_pelicula', methods=['GET', 'POST'])
def borrar_pelicula():
    if request.method == 'GET':
        return render_template('Pelicula/borrar_pelicula.html')
    else:
        idPelicula = request.form['idPelicula']

        pelicula_a_eliminar = Pelicula.query.get(idPelicula)
        #nuevo_usuario = Usuario(nombre=nombre, password=password, email=email)
        if pelicula_a_eliminar:
            db.session.delete(pelicula_a_eliminar)
            db.session.commit()
            return 'Pelicula eliminada'
            flash('Pelicula eliminada correctamente', 'success')
        else:
            return 'Pelicula no encontrada'