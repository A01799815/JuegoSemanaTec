from turtle import *
from random import randrange, choice
from freegames import square, vector

#Lista que contiene los colores posibles para la serpiente y la comida
colors = ['blue', 'green', 'purple', 'orange', 'yellow']

def generate_color():
    "Funcion que escoge un color de la lista"
    return choice(colors)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Genera los colores aleatorios para cada variable
snake_color = generate_color()
food_color = generate_color()

# Se comprueba que los colores generados son diferentes, de lo contrario se cambia el color de la comida. 
if snake_color == food_color:
    food_color = generate_color()

def change(x, y):
    "Cambia la direccion del movimiento de la serpiente"
    aim.x = x
    aim.y = y

def inside(head):
    "TRUE si la cabeza de la serpiente esta dentro del area de juego"
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Mover la serpiente una casilla"
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    else:
        snake.pop(0)

    clear()
    
    # Generar movimientos aleatorios de la comida. Se ejecuta aleatoriamente una de cada 10 veces para reducir la velocidad
    if(choice(range(10))) == 0:
        dx, dy = choice([-10, 0, 10]), choice([-10, 0, 10])
        food.x += dx
        food.y += dy

    # Verificar límites de la ventana y hacer que la comida se mueva.
    if not inside(food):
        if food.x < -200 or food.x > 190:
            dx = -dx
        if food.y < -200 or food.y > 190:
            dy = -dy
        food.x += dx
        food.y += dy


    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

