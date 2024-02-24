def salir():
    print("Saliendo")
    exit()

def verRegistro():
    print(" ")

def op1():
    print("Ver los registros de una tabla")
print("Seleccione la tabla de la que desea ver los registros")

while True:
    print("1. Tabla peliculas")
    print("2. Tabla ")
    print("3. Tabla ")
    print("4. Salir")
    opp = input("Seleccione el numero que indica lo que desea hacer: ")

    if opp == "1":
        print("Tabla peliculas")
    elif opp == "2":
        print("Tabla ")
    elif opp == "3":
        print("Tabla ")
    elif opp == "4":
        salir()
    else:
        print("Opcion invalida. Vuelva a intentarlo.")

def filtraRegistro():
    print(" ")

def op2():
    print("Filtra los registros de una tabla por id")
    filtraRegistro()
def actualizaRegistro():
    print(" ")

def op3():
    print("Actualizar la columna de un registro")
    #nombre y para el caso Renta, modificar la fecha de la renta
    actualizaRegistro()
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