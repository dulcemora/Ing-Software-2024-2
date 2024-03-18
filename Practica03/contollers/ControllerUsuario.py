from flask import Blueprint, request, render_template, flash, redirect, url_for
from alchemyClasses.Usuario import Usuario, db
from model.Model_usuario import borra_usuario
from sqlalchemy.exc import IntegrityError

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/', methods=['GET'])
def raiz():
    return render_template('Usuario/raiz.html')

@usuario_blueprint.route('/ver_usuarios', methods=['GET'])
def ver_usuarios():
    usuarios = Usuario.query.all()

    for usuario in usuarios:
        print(f"ID: {usuario.idUsuario}, Nombre: {usuario.nombre}, Email: {usuario.email}")
    #usuarios = Usuario.query.all()
    return render_template('Usuario/ver_usuarios.html', usuarios=usuarios)

@usuario_blueprint.route('/agregar_usuario', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombr = request.form['nombre']
        ap_pat = request.form['apPat']
        ap_mat = request.form['apMat']
        passwd = request.form['password']
        mail = request.form['email']
        #profilePictureU = request.form['profilePicture']
        #superUserU = request.form['superUser']

        nuevo_usuario = Usuario(nombre=nombr, apPat=ap_pat, apMat=ap_mat, password=passwd, email=mail,
                                profilePicture=None, superUser=0)
        try:
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Usuario agregado correctamente', 'success')
            return redirect(url_for('usuario.agregar_usuario'))
        except IntegrityError:
            db.session.rollback()  # Revertir los cambios realizados en la transacción
            flash('Error: El correo electrónico ya está registrado', 'error')
            return redirect(url_for('usuario.agregar_usuario'))

    return render_template('Usuario/agregar_usuario.html')



@usuario_blueprint.route('/borrar_usuario', methods=['GET', 'POST'])
def borrar_usuario():
    if request.method == 'GET':
        return render_template('Usuario/borrar_usuario.html')
    else:
        idUsuario = request.form['idUsuario']

        usuario_a_eliminar = Usuario.query.get(idUsuario)
        #nuevo_usuario = Usuario(nombre=nombre, password=password, email=email)
        if usuario_a_eliminar:
            db.session.delete(usuario_a_eliminar)
            db.session.commit()
            return 'Usuario eliminado'
            flash('Usuario eliminado correctamente', 'success')
        else:
            return 'Usuario no encontrado'

'''
@usuario_blueprint.route('/actualizar_usuario', methods=['POST'])
def actualizar_usuario():
    id_usuario = request.form['idUsuario']
    actualiza = request.form['campoActualizar']
    nuevo_valor = request.form['nuevoValor']
    cursor = db.cursor()

#    try:
    sql = f"UPDATE usuarios SET {actualiza} = %s WHERE id = %s"
    cursor.execute(sql, (nuevo_valor, id_usuario))
    db.session.commit()
#        mensaje = f"{actualiza.capitalize()} del usuario con ID {id_usuario} actualizado correctamente a '{nuevo_valor}'"
#    except mysql.connector.Error as error:
#        mensaje = f"Error al actualizar el campo del usuario: {error}"
    return render_template('Usuario/actualizar_usuario.html')
'''