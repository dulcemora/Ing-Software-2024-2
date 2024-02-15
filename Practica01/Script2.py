def cuentavalles(cadena):
    #U indica paso hacia arriba
    #D indica paso hacia abajo
    nivel = 0
    valles = 0

    for letra in cadena:
        if letra == 'U':
            nivel += 1
        elif letra == 'D':
            nivel -= 1
        else:
            print("Se ingreso una letra invalida")

        if nivel == 0 and letra == 'U':
            valles += 1
            

    return valles

def cuentamontanas(cadena):
    #U indica paso hacia arriba
    #D indica paso hacia abajo
    nivel = 0
    montanas = 0

    for letra in cadena:
        if letra == 'U':
            nivel += 1
        elif letra == 'D':
            nivel -= 1
        else:
            print("Se ingreso una letra invalida")

        if nivel == 0 & letra == 'D':
            montanas += 1

    return montanas

#print("La cantidad de montanas recorridas es: ", cuentamontanas(cadena))

class Nodo:
    def __init__(self, contenido):
        self.contenido = contenido
        self.izq = None
        self.der = None

class ArbolBinarioOrdenado:
    def __init__(self, contenidoAB):
        self.contenidoAB = Nodo(contenidoAB)
    
    def agregaElem(self, contenido, nodo):
        if nodo == None:
            nodo = self.raiz
        
        if contenido < nodo.contenido:
            if nodo.izq == None:
                nodo.izq = Nodo(contenido)
            else:
                self.agregaElem(contenido, nodo.izq)
        else:
            if nodo.der == None:
                nodo.der = Nodo(contenido)
            else:
                self.agregaElem(contenido, nodo.der)

    def preorden(raiz):
        if raiz != None:
            print(raiz.contenido)
            preorden(raiz.izq)
            preorden(raiz.der)             

    def inorden(raiz):
        if raiz != None:
            inorden(raiz.izq)
            print(raiz.contenido)
            inorden(raiz.der)             

    def postorden(raiz):
        if raiz != None:
            postorden(raiz.der)
            postorden(raiz.izq)
            print(raiz.contenido)             


def menu():
    print("Bienvenido al menu(Seleccione el numero de la opcion a realizar):")
    print("1. Ejercicio valles y montanas")
    print("2. Ejercicio Arbol Binario")
    print("3. Salir")

def menu2():
    print("¿Que desea contar?(Seleccione el numero de la opcion a realizar):")
    print("1. valles")
    print("2. montanas")
    print("3. regresar")

def menu3():
    print("¿Que desea hacer?(Seleccione el numero de la opcion a realizar):")
    print("1. Agregar elemento")
    print("2. Preorden")
    print("3. Inorden")
    print("4. Postorden")
    print("5. Regresar")

def op1():
    while True:
        menu2()
        seleccion = input("seleccione una opcion: ")

        if seleccion == "1":
            print("Cuenta valles")
            cadena = input("Ingrese la cadena \n")
            print("La cantidad de valles recorridos es: ", cuentavalles(cadena))
        elif seleccion == "2":
            print("Cuenta montanas")
            cadena = input("Ingrese la cadena \n")
            print("La cantidad de montanas recorridos es: ", cuentamontanas(cadena))
        elif seleccion == "3":
            print("Escogio regresar")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def op2():
    while True:
        menu3()
        seleccion = input("seleccione una opcion: ")

        if seleccion == "1":
            print("Agrega elemento")
            elem = input("Ingrese el elemento a agregar \n")
            agregaElem(self, elem, Nodo)
        elif seleccion == "2":
            print("Preorden")
            preorden(raiz)
        elif seleccion == "3":
            print("Inorden")
            inorden(raiz)
        elif seleccion == "4":
            print("Postorden")
            postorden(raiz)
        elif seleccion == "5":
            print("Escogio regresar")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def main():
    while True:
        menu()
        seleccion = input("Por favor, seleccione una opción: ")

        if seleccion == "1":
            op1()
        elif seleccion == "2":
            op2()
        elif seleccion == "3":
            print("Escogio Salir, vuelva pronto!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
