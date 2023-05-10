from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0 #Se define la variable para contar los tabs


def square(x, y):
    '''Dibuja recuadro en la coordenada indicada
    x: coordenada X
    y: coordenada y'''
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convierte coordenadas (x,y) en indice de recuadro"""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convierte indice de recuadro en coordernadas (x,y)"""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Actualiza Mark, recuadros ocultos y cuenta de clics."""
    global tap_count
    tap_count += 1 #Tras ejecutarse la función, la variable adquiere un nuevo valor
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        

#Imprime el contador de TAPS en la pantalla del juego 
def display_tap_count():
    ''' Muestra la cuenta de clics'''
    up()
    goto(0, -180)
    color('black')
    write('Taps: ' + str(tap_count), align='center',
          font=('Arial', 20, 'normal'))


def draw():
    """Dibuja la imagen y los recuadros, muestra el numero del indice del recuadro"""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x+25,y) # Ubica la tortuga a la mitad de cada recuadro (coordenada x + 25 puntos)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'),align="center") #Escribe el numero centrado

#Se define una varible en la cual se cuentan si los objetos de la lista hide tienen valor TRUE, 
#al llegar a 0, se procede a llamar a la funcion que imprime el mensaje final
    if all(not x for x in hide): 
        display_final()

    display_tap_count()
    update()
    ontimer(draw, 100)
#Funcion para imprimir el mensaje final
def display_final():
    up()
    goto(0, 0)
    color('white')
    write('Todos los cuadros han sido destapados', align='center',
          font=('Arial', 15, 'normal'))

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
