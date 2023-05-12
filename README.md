## README Proyecto Freegames
En esta entrega de reppsitorio, se pretende adjuntar el trabajo realizado durante la semana tec que tiene como nombre "Herramientas computacionales: El arte de la programación".<br>Se muestran cinco codigos de juegos clasicos, pertenecientes a la librería "Freegames" de python:

<ol>
  <li>Paint</li>
  <li>Snake</li>
  <li>Pacman</li>
  <li>Cannon</li>
  <li>Memory</li>
</ol>
  
En cada uno de estos juegos se requirio de la modificación de algun aspecto en el codigo de estos,
con el fin de que mejoremos nuestras habilidades de logica y programación, ademas de perfeccionar en cierta medida estos juegos. 

## Descripcion de lo realizado para cada juego

<ol>
  <li>Paint</li>
  En este juego se solicito que se añadiera:
  <ol>
    <li>Un color nuevo</li>
    <li>Dibujar un circulo</li>
    <li>Completar el rectangulo</li>
    <li>Completar el triangulo</li>
  </ol>
  <li>Snake</li>
  En este juego se solicito que se añadiera:
  <ol>
    <li>La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana</li>
    <li>Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes entre sí, pero al azar, de una serie de 5 diferentes colores, excepto el rojo</li>
  </ol>
  <li>Pacman</li>
  En este juego se solicito que se añadiera:
  <ol>
    <li>Los fantasmas sean más listos</li>
    <li>Cambiar el tablero</li>
    <li>Historia de los commits del repositorio</li>
  </ol>
  <li>Cannon</li>
  En este juego se solicito que se añadiera:
  <ol>
    <li>La velocidad del movimiento para el proyectil y los balones sea más rápida</li>
    <li>Hacer que el juego nunca termine, de manera que los balones al salir de la ventana se re posicionen.</li>
  </ol>
  <li>Memory</li>
  En este juego se solicito que se añadiera:
  <ol>
    <li>La velocidad del movimiento para el proyectil y los balones sea más rápida</li>
    <li>Hacer que el juego nunca termine, de manera que los balones al salir de la ventana se re posicionen.</li>
  </ol>
</ol> 

 ## Preparación del ambiente
 Para esta actividad se requirio de los siguientes elementos 
 <ul>
  <li>Instalación de Python 3 </li>
  <li>Instalación de PIP</li>
 </ul>
 
 ## Instalación 🔧

Para reafirmar que la instalación de pip haya sido correcta y completa, nos podemos apoyar del siguiente comando que rectificara la versión de pip instalada en el dispositivo:

```
pip --version
```

Tras obtener la ultima versión de Python 3.X que trae consigo el instalador "pip", se solicitó la instalación de la librería freegames que trae consigo un total de 17 juegos diferentes, esta acción se puede realizar directamente desde "Símbolo del Sistema" ó desde alguna de las distintas interfaces de manipulación de consola (Ubuntu/PowerShell/Git Bash), haciendo uso del siguiente comando:

```
python3 -m pip install freegames
```

## Ejecutando las pruebas - Librería freegames ⚙️

Para consultar el contenido de la librería es posible usar este comando que desplegará la lista de todos los juegos incluidos en la librería:
```
python3 -m freegames list
```
Tras seleccionar cualquier juego de interés, es posible correr el juegos desde la consola con el siguiente comando:
```
python3 -m freegames.snake
```
Los juegos se pueden modificar copiando su código fuente, este se puede obtener a partir del siguiente comando que creará una copia del archivo en nuestro directorio local:
```
python3 -m freegames copy snake
python3 snake.py

  
