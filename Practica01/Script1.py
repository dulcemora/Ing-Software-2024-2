import random

# Variable que almacena los sets ganados por el primer jugador
setsJug1 = 0
# Variable que almacena los sets ganados por el segundo jugador
setsJug2 = 0

# Función que da los puntos
def cuentaPuntos(puntosTotal, puntosOponente):
    if puntosTotal == 0:
        puntosTotal = 15
    elif puntosTotal == 15:
        puntosTotal = 30
    elif puntosTotal == 30:
        puntosTotal = 40
    elif puntosTotal == 40:
        if puntosOponente == 40:
            puntosTotal = 'advantage'
        elif puntosOponente == 'advantage':
            puntosOponente = 40
        else:
            puntosTotal = 'game'
    return puntosTotal

# Función que define los saques
def saque():
    if random.randint(0, 1) == 0:
        return "El saque le corresponde a " + jug1
    else:
        return "El saque le corresponde a " + jug2

# Función que define el cambio de cancha
def cambioCancha(juegosJug1, juegosJug2):
    if (juegosJug1 + juegosJug2) % 2 != 0:
        return "Cambio de cancha"
    else:
        return "Cambio de cancha"

# Función que define cómo es un set
def set():
    # Variable que almacena los juegos ganados por el primer jugador en un set
    juegosJug1 = 0
    # Variable que almacena los juegos ganados por el segundo jugador en un set
    juegosJug2 = 0

    # Variable que almacena los puntos ganados por el primer jugador
    puntosJug1 = 0
    # Variable que almacena los puntos ganados por el segundo jugador
    puntosJug2 = 0

    print(saque())
    print(cambioCancha(juegosJug1, juegosJug2))

    while abs(juegosJug1 - juegosJug2) < 2:
        while puntosJug1 != 'game' or puntosJug2 != 'game':
        #while puntosJug1 != 'game' or puntosJug2 != 'game' or (juegosJug1 < 6 or juegosJug2 < 6):    

            try:
                seleccion = int(input("¿Que jugador desea que gane? (1 o 2): "))
                if seleccion == 1:
                    puntosJug1 = cuentaPuntos(puntosJug1, puntosJug2)
                    print(jug1, " gana puntos. Puntos al momento:", puntosJug1)
                elif seleccion == 2:
                    puntosJug2 = cuentaPuntos(puntosJug2, puntosJug1)
                    print(jug2, " gana puntos. Puntos al momento:", puntosJug2)
                else:
                    print("No ingreso un numero valido")
            except:
                print("Ingrese un numero, por favor")

        # Verificar quién gana el juego
        if puntosJug1 == 'game':
            print(jug1, " gana el juego")
            juegosJug1 += 1
        elif puntosJug2 == 'game':
            print(jug2, " gana el juego")
            juegosJug2 += 1

        # Reiniciar los puntos para el próximo juego
        puntosJug1 = 0
        puntosJug2 = 0

        # Verificar si se necesita cambio de cancha y saque para el próximo juego
        if juegosJug1 < 6 or juegosJug2 < 6:
            cambioCancha(juegosJug1, juegosJug2)
            saque()

    # Verificar quién gana el set
    if juegosJug1 > juegosJug2:
        print(jug1, " gana el set")
        global setsJug1
        setsJug1 += 1
    else:
        print(jug2, " gana el set")
        global setsJug2
        setsJug2 += 1


# Función para jugar un partido completo
def op1():
    global setsJug1
    global setsJug2

    while setsJug1 < 2 and setsJug2 < 2:
        set()

    if setsJug1 > setsJug2:
        print("El ganador es ", jug1)
    else:
        print("El ganador es ", jug2)


# Función para mostrar el menú
def menu():
    global jug1
    global jug2

    print("----------JUGAR----------")
    jug1 = input("Ingrese el nombre del primer jugador: ")
    jug2 = input("Ingrese el nombre del segundo jugador: ")


def main():
        
        menu()
        op1()

if __name__ == "__main__":
    main()