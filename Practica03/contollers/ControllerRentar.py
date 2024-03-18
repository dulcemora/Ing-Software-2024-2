from flask import Blueprint, request, render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError
from alchemyClasses.Rentar import Rentar, db
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula

rentar_blueprint = Blueprint('rentar', __name__, url_prefix='/rentar')

@rentar_blueprint.route('/', methods=['GET'])
def raiz():
    return render_template('Rentar/raizrentar.html')

@rentar_blueprint.route('/ver_rentas', methods=['GET'])
def ver_rentas():
    rentas = db.session.query(Rentar, Usuario, Pelicula).join(Usuario).join(Pelicula).all()
#    rentas = Rentar.query.all()
    return render_template('Rentar/ver_rentas.html', rentas=rentas)

@rentar_blueprint.route('/agregar_renta', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'POST':
        id_usuario = request.form['idUsuario']
        id_pelicula = request.form['idPelicula']
        fecha_renta = request.form['fecha_renta']
        dias_de_renta = request.form['dias_de_renta']
#        estatus = request.form['estatus']

        nueva_renta = Rentar(id_usuario=id_usuario, id_pelicula=id_pelicula, fecha_renta=fecha_renta,
                             dias_de_renta=dias_de_renta, estatus=True)
        db.session.add(nueva_renta)
        db.session.commit()
        return redirect(url_for('renta.ver_rentas'))

    usuarios = Usuario.query.all()
    peliculas = Pelicula.query.all()
    return render_template('Rentar/agregar_renta.html', usuarios=usuarios, peliculas=peliculas)

'''
@pelicula_blueprint.route('/actualizar_pelicula', methods=['GET', 'POST'])
def actualizar_pelicula():
    if request.method == 'POST':
        id_pelicula = int(request.form['idPelicula'])
        actualiza = request.form['campoActualizar']
        nuevo_valor = request.form['nuevoValor']

        pelicula = Pelicula.query.get(id_pelicula)
        if pelicula:
            if hasattr(pelicula, actualiza):
                setattr(pelicula, actualiza, nuevo_valor)
                db.session.commit()
                flash('Pelicula actualizado', 'success')
                return render_template('Pelicula/actualizar_pelicula.html')
            else:
                flash('No se puede actualizar el campo', 'error')
        else:
            flash('Pelicula no encontrada', 'error')
    return render_template('Pelicula/actualizar_pelicula.html')
'''