from graphics import *
from time import *

# Funciones internas
    # Gráficas
def elec1(sublv):
    sublv=sublv-1
    electron1 = Circle(Point(50, lv[sublv]), 20)
    electron1.setFill('blue')
    e1 = electron1.draw(sim)
    return e1
    
def elec2():
    electron2 = Circle(Point(150, lv[0]), 20)
    electron2.setFill('red')
    e2 = electron2.draw(sim)
    return e2

def simlayout(sublv, sim):
    sub[sublv] = Line(Point(0, lv[sublv]), Point(200, lv[sublv]))
    sub[sublv].draw(sim)
    Text(Point(205, lv[sublv]), (sublv+1)).draw(sim)
    Text(Point(50, 505), "e1").draw(sim)
    Text(Point(150, 505), "e2").draw(sim)

def ser(x):
    return {
        'Lyman': 1,
        'Balmer': 2,
        'Paschen': 3,
        'Bracket': 4,
        'Pfund': 5
    }.get(x,0)
    
def movement(new_sublv, serie):
    new_sublv=new_sublv-1
    mov_e2 = (lv[new_sublv]-475)
    mov_e1 = -((lv[new_sublv]+75*ser(serie))-75-475)
    # Validación para determinar si el subnivel es suficiente para cierta serie
    if(ser(serie) > new_sublv):
        print("No es posible utilizar esta serie en este subnivel")
        return 0
    for i in range(46):
        e2.move(0, mov_e2/46)
        sleep(.05)
    for j in range(46):
        e1.move(0, mov_e1/46)
        sleep(.05)

    # Cálculos

def long_onda(serie, ni):
    serie = ser(serie)
    R = 1.097*(10**7)
    delta = R*((1/(serie**2))-(1/(ni**2)))
    delta = 1/delta
    return delta

def excitacion(Z, n):
    energia = 13.6*(Z**2)*(1-(1/(n**2)))
    return energia

def emitida(Z, n, nf):
    energia_i = -(13.6*(Z**2))/n
    energia_f = -(13.6*(Z**2))/nf
    energia = energia_i - energia_f
    return energia
    

# Alturas definidas para cada subnivel
lv = [475, 400, 325, 250, 175, 100, 25]
invlv = [25, 100, 175, 250, 325, 400, 475]

# Array con los subniveles
sub = [1, 2, 3, 4, 5, 6, 7]

#Variable infinity para hacer que el programa se cicle indefinidamente hasta que el usuario decida cerrar la teminal
infinity = True

#Titulo del programa en la terminal
print("====SIMULADOR DE EXITACION DE UN ELECTRON===")

# Loop infinito hasta que el usuario decida cerrar la terminal
while infinity == True:
    
    # Abrir la ventana principal   
    sim = GraphWin('Simulador de exitación de un electrón', 215, 520)

    # Layout para las gráficas
    for i in range (7):
        simlayout(i, sim)

# TEST
    # Inicialización en cada ciclo de algunas variables a validar
    target=''
    e1_input=-1
    mov = ''
    
    numatom=0

    # Introducción y validación de la posición del primer electrón
    while (e1_input > 7 or e1_input < 0):
        e1_input= input('\nIntroduzca el subnivel del primer electron: ')
        e1_input = int(e1_input)
        if (e1_input > 7 or e1_input < 1):
            print("Subnivel invalido, intente de nuevo")
        elif (e1_input==1):
            print("No puede haber excitacion si ambos electrones estan en el mismo nivel!")

    # Dibujo de los electrones
    e1 = elec1(e1_input)
    e2 = elec2()

    # Introducción y validación de la serie a utilizar
    while (ser(target)==0 or mov==0):
        target = input('\nIngrese el tipo de serie que utilizara (Lyman, Balmer, Paschen, Bracket, Pfund): ')
        if (ser(target)==0):
            print("Serie invalida, intente de nuevo")
        # Movimiento de los electrones
        else:
            mov = movement(e1_input, target)

    # Cálculo de la Longitud de Onda, la Energía de Exitación y Energía Emitida
    delta = long_onda(target, e1_input)
    ex = excitacion(1, e1_input)
    ee = emitida(1, e1_input, ser(target))
    print("Longitud de onda =", delta, "m")
    print("Energia de excitacion =", format(ex, '.2f'), "eV")
    print("Energia emitida =", format(ee, '.2f'), "eV")
    # Mensaje del fin de ciclo
    print("\nHaga click en la simulación para reiniciar o cierre esta ventana para terminar")
    sim.getMouse()
    sim.close()
