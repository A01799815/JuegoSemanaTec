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
  <ul>
    <li>Un color nuevo</li>
    <li>Dibujar un circulo</li>
    <li>Completar el rectangulo</li>
    <li>Completar el triangulo</li>
  </ul>
  En este juego, gracias a funciones ya existentes, se pudo trabajar con estas para modificarlas y poder asi obtener los puntos solicitados. 
  <li>Snake</li>
  En este juego se solicito que se añadiera:
  <ul>
    <li>La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana</li>
    <li>Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes entre sí, pero al azar, de una serie de 5 diferentes colores, excepto el rojo</li>
  </ul>
  Fue necesario el pensamiento logico, para asi poder crear nuevas funciones que afectaran al codigo y cumplir asi los puntos solicitados. 
  <li>Pacman</li>
  En este juego se solicito que se añadiera:
  <ul>
    <li>Los fantasmas sean más listos</li>
    <li>Cambiar el tablero</li>
    <li>Historia de los commits del repositorio</li>
  </ul>
  Se modifico el codigo ya establecido, ademas, se añadio algo de pensamieto logico, para hacer que el fantasma volte hacia donde esta pacman y tome una decisión al topar con pared.
  <li>Cannon</li>
  En este juego se solicito que se añadiera:
  <ul>
    <li>La velocidad del movimiento para el proyectil y los balones sea más rápida</li>
    <li>Hacer que el juego nunca termine, de manera que los balones al salir de la ventana se re posicionen.</li>
  </ul>
  Se elimino una parte del codigo, para lograr la continuación del juego, ademas de modificar calores dentro de este codigo para hacer el juego mas rapido. 
  <li>Memory</li>
  En este juego se solicito que se añadiera:
  <ul>
    <li>Contar y desplegar el numero de taps</li>
    <li>Detectar cuando todos los cuadros se han destapado</li>
    <li>Centrar el dígito en el cuadro</li>
    <li>Como un elmento de innovación al juego, podrías utilizar algo diferente a los dígitos para resolver el juego y que al usuario le ayude a tener mejor memoria?</li>
  </ul>
  Mediante las funciones que ya existen en el codigo, se manipularon para agregar los puntos solicitados. <br> En el ultimo punto solicitado, se podria asignar colores a los numeros o al voltear las casillas, usando colores similares para numeros cercanos entre si para ubicarlos y distinguirlos de otros alrededor mas facilmente.
</ol> 

 ## Preparación del ambiente
 Para esta actividad se requirio de los siguientes elementos 
 <ul>
  <li>Instalación de Python 3 </li>
  <li>Instalación de PIP</li>
 </ul>
 
 ## Instalación 

Para reafirmar que la instalación de pip haya sido correcta y completa, nos podemos apoyar del siguiente comando que rectificara la versión de pip instalada en el dispositivo:

```
pip --version
```

Tras obtener la ultima versión de Python 3.X que trae consigo el instalador "pip", se solicitó la instalación de la librería freegames que trae consigo un total de 17 juegos diferentes, esta acción se puede realizar directamente desde "Símbolo del Sistema" ó desde alguna de las distintas interfaces de manipulación de consola (Ubuntu/PowerShell/Git Bash), haciendo uso del siguiente comando:

```
python3 -m pip install freegames
```

## Ejecutando las pruebas - Librería freegames 

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
```
## Autores
#### José Eduardo Rosas Ponciano - A01784461
#### Cesar Antonio Espinosa Madrid - A01799815
