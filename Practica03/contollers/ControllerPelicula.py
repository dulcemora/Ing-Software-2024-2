from flask import Blueprint, request, render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError
from alchemyClasses.Pelicula import Pelicula, db

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/', methods=['GET'])
def raiz():
    return render_template('Pelicula/raizpelicula.html')

@pelicula_blueprint.route('/ver_peliculas', methods=['GET'])
def ver_peliculas():
    peliculas = Pelicula.query.all()
    return render_template('Pelicula/ver_peliculas.html', peliculas=peliculas)


@pelicula_blueprint.route('/agregar_pelicula', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'POST':
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']

        nueva_pelicula = Pelicula(nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)
        try:
            db.session.add(nueva_pelicula)
            db.session.commit()
            flash('Película agregada correctamente', 'success')
            return redirect(url_for('pelicula.agregar_pelicula'))
        except IntegrityError:
            db.session.rollback()  # Revertir los cambios realizados en la transacción
            flash('Error: El correo electrónico ya está registrado', 'error')
            return redirect(url_for('pelicula.agregar_pelicula'))

    return render_template('Pelicula/agregar_pelicula.html')


@pelicula_blueprint.route('/borrar_peliculas', methods=['GET', 'POST'])
def borrar_peliculas():
    if request.method == 'GET':
        return render_template('Pelicula/borrar_peliculas.html')
    else:
        idPelicula = request.form['idPelicula']

        pelicula_a_eliminar = Pelicula.query.get(idPelicula)
        if pelicula_a_eliminar:
            db.session.delete(pelicula_a_eliminar)
            db.session.commit()
            flash('Pelicula eliminado correctamente', 'success')
            return redirect(url_for('pelicula.borrar_peliculas'))
        else:
            flash('Error: No se encontró la película', 'error')
            return redirect(url_for('pelicula.borrar_peliculas'))