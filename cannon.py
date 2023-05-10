from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    '''Inicializa posicion y velocidad de la bola al hacer click fuera del area de juego'''
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 20    #Se reduce el dividendo para aumentar la velocidad inicial
        speed.y = (y + 200) / 20    #Se reduce el dividendo para aumentar la velocidad inicial

def inside(xy):
    '''Evalua si el argumento esta dentro del area de juego'''
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    '''Dibuja la bola y los objetivos'''
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    '''Actualiza la posicion y velocidad en Y de la bola, y los objetivos para dar movimiento'''
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1.5 # Aumenta el valor para que los targets se muevan mas rapido

    if inside(ball):
        speed.y -= 0.5  #Aumenta el valor para que la bola descienda mas rapido
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()
    
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()
#Al eliminar el siguinte ciclo for del codigo, se logra que el juego no termine
    '''for target in targets:
        if not inside(target):
            return'''

    ontimer(move, 15) # Se reduce el valor del segundo argumento: reduce el tiempo de retraso al ejecutar la funcion.

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
