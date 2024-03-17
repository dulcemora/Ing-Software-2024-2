from flask import Blueprint, request, render_template, flash, url_for
from random import randint

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/') #localhost:5000/usuario/
def ver_usuarios():
    return "select * from usuario"

#responde a localhost:5000/usuario/id/1
@usuario_blueprint.route('/id/<int:id_usuario>/<string:nombre>') #<tipo:nombre_variable>
def ver_usuario_id(id_usuario, nombre):
    return f"Se hace el query con el id {id_usuario} y el nombre {nombre}"


@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'GET':
        return render_template('Usuario/add_user.html')
    else:
        #Obtengo la información del método post.
        name = request.form['name']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        num_cta = request.form['num_cta']
        passwd = request.form['passwd']

        #Creo la pelicula.
#pelicula = Pelicula(name, ap_pat, ap_mat, num_cta, passwd)

 #       db.session.add(pelicula)
  #      db.session.commit()

   #     flash('Usuario creado exitosamente', 'success')

#        return redirect(url_for('inicio'))
    #    return url_for('inicio')

        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('usuario.agregar_usuario')
        # Y regreso al flujo que me hayan especificado.
        return render_template('Usuario/user_added.html', name=name, num_cta=num_cta)