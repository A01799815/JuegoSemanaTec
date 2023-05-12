from turtle import *
from freegames import vector

def line(start, end):
    "Dibuja una linea desde el punto inicial al punto final"
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Dibuja un cuadrado desde el punto inicial al punto final"
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Se utiliza la funcion predeterminada circle()
#Se renombro la funcion como 'circle_' para evitar errores en la ejecucion al usar tambien la funcion predeterminada circle()
def circle_(start, end):    
    "Dibuja un circulo desde el punto inicial alrededor del punto indicado como punto final"
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    radius = abs(start - end)
    circle(radius)
    
    end_fill()
    

#Se utliza el mismo metodo del cuadrado, añadiendo las coordenadas del punto final y cambiando el rango de lineas a dibujar.
def rectangle(start, end):
    "Dibuja un rectangulo con diagonal desde el punto inical al punto final."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
    end_fill()
    
#Se utliza el mismo metodo del cuadrado, cambiando el rango para que dibuje 3 lineas y # el angulo left cambiarlo a 120
def triangle(start, end):
    "Dibuja un triangulo equilatero desde y hasta el punto inicial. El valor del lado es la distancia al punto final."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y):
    "Guarda las coordenadas del punto incial si no hay ninguno o dibuja una figura."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Guarda el valor del estado actual del dibujo"
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P') # Se añadio un nuevo color
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle_), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
