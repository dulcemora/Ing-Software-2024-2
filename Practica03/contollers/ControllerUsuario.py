from flask import Blueprint, request, render_template, flash, redirect, url_for
from alchemyClasses.Usuario import Usuario, db
from model.Model_usuario import borra_usuario

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/', methods=['GET'])
def raiz():
    return render_template('Usuario/raiz.html')

@usuario_blueprint.route('/ver_todos', methods=['GET'])
def ver_usuarios():
    usuarios = Usuario.query.all()

    for usuario in usuarios:
        print(f"ID: {usuario.idUsuario}, Nombre: {usuario.nombre}, Email: {usuario.email}")
    #usuarios = Usuario.query.all()
    return render_template('Usuario/ver_todos.html', usuarios=usuarios)

@usuario_blueprint.route('/id/<int:id_usuario>/<string:nombre>')
def ver_usuario_id(id_usuario, nombre):
    usuario = Usuario.query.filter_by(idUsuario=id_usuario).first()
    if usuario:
        return f"Nombre: {usuario.nombre}, Email: {usuario.email}"
    else:
        return "Usuario no encontrado"

@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'GET':
        return render_template('Usuario/add_user.html')
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

@usuario_blueprint.route('/borrar',  methods=['GET', 'POST'])
def borrar_usuario():
    #borra_usuario(1)
    #print("Borrado con éxito!")
    return "borrar"