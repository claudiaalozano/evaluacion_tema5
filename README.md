# evaluacion_tema5
Dirección de Github: https://github.com/claudiaalozano/evaluacion_tema5.git

### Ejercicio1:
```
#creo la función para la suma
def suma(a,b):
    try:
        resultado = a + b
    except TypeError:
        print("Error: Los valores introducidos nos son validos")
        resultado = None
    return resultado

#creo la función para la resta
def resta(a,b):
    try:
        resultado = a-b
    except TypeError:
        print("Error: Los valores introducidos nos son validos")
        resultado = None
    return resultado

#creo la función para la multiplicación
def multiplicacion(a,b):
    try:
        resultado = a*b
    except TypeError:
        print("Error: Los valores introducidos nos son validos")
        resultado = None
    return resultado

#creo la función para la división
def division(a,b):
    try:
        resultado = a/b
    except TypeError:
        print("Error: Los valores introducidos nos son validos")
        resultado = None
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")
        resultado = None
    return resultado
```

### Ejercicio2:
```
import sys

#vamos a abrir el fichero contador.txt en modo lectura
try:
    with open("contador.txt", "r") as f:
        contador = int(f.read())

except FileNotFoundError:
    with open("contador.txt", "w") as f:
        f.write("0")
        contador = 0

except ValueError:
    print("Error: El valor no es un número")
    sys.exit(1)

if len(sys.argv)>1 and sys.argv[1] == "inc":
    contador += 1

if len(sys.argv)>1 and sys.argv[1] == "dec":
    contador -= 1

print(contador)

with open("contador.txt", "w") as f:
    f.write(str(contador))
 ```

### Ejercicio3:

```
import pickle

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

class Gestor:
    def __init__(self):
        self.personajes = []

    def agregar_personaje(self, personaje):
        if personaje.nombre not in self.personajes:
            self.personajes.append(personaje)

    def mostrar_personaje(self):
        for personaje in self.personajes:
            print("Nombre: {}".format(personaje.nombre))
            print("Vida: {}".format(personaje.vida))
            print("Ataque: {}".format(personaje.ataque))
            print("Defensa: {}".format(personaje.defensa))
            print("Alcance: {}".format(personaje.alcance))
            print()

    def borrar_personaje(self, nombre):
        if nombre in self.personajes:
            del self.personajes[nombre]

    def guardar(self):
        with open("personajes", "wb") as f:
            pickle.dump(self.personajes, f)
    ```

### Ejercicio4:

```
import datetime
import time
import os

while True:
    hora_actual = datetime.datetime.now()
    print(hora_actual.strftime("%H:%M:%S"))
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
```
