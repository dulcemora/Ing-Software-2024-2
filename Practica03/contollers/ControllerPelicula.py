from flask import Blueprint, request, render_template, flash, url_for
from random import randint

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/', methods=['GET'])
def raizpelicula():
    return render_template('Pelicula/raizpelicula.html')

@pelicula_blueprint.route('/ver_peliculas', methods=['GET'])
def ver_peliculas():
    peliculas = Pelicula.query.all()

    for pelicula in peliculas:
        print(f"ID: {pelicula.idUsuario}, Nombre: {pelicula.nombre}, Email: {pelicula.email}")
    return render_template('Pelicula/ver_peliculas.html', peliculas=peliculas)

'''
@pelicula_blueprint.route('/agregar_pelicula', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'GET':
        return render_template('Usuario/agregar_usuario.html')
    else:
        nombre = request.form['name']
        password = request.form['password']
        email = request.form['email']
        # Puedes manejar otros campos como la imagen de perfil y si es superusuario aquí
        nuevo_usuario = Usuario(nombre=nombre, password=password, email=email)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario agregado correctamente', 'success')
        return "Usuario agregado"
        #return redirect(url_for('usuario.ver_usuarios'))

@usuario_blueprint.route('/borrar_usuario', methods=['GET', 'POST'])
def borrar_usuario():
    if request.method == 'GET':
        return render_template('Usuario/borrar_usuario.html')
    else:
        idUsuario = request.form['idUsuario']
        # Puedes manejar otros campos como la imagen de perfil y si es superusuario aquí
        usuario_a_eliminar = Usuario.query.get_or_404(idUsuario)
        #nuevo_usuario = Usuario(nombre=nombre, password=password, email=email)
        if usuario_a_eliminar:
            db.session.delete(usuario_a_eliminar)
            db.session.commit()
            return 'Usuario eliminado'
        else:
            return 'Usuario no encontrado', 404
        flash('Usuario eliminado correctamente', 'success')
        return render_template('Usuario/borrar_usuario.html')
'''