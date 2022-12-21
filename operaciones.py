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
        resultado = a - b
    except TypeError:
        print("Error: Los valores introducidos nos son validos")
        resultado = None
    return resultado

#creo la función para la multiplicación
def multiplicacion(a,b):
    try:
        resultado = a * b
    except TypeError:
        print("Error: Los valores introducidos nos son validos")
        resultado = None
    return resultado

#creo la función para la división
def division(a,b):
    try:
        resultado = a / b
    except TypeError:
        print("Error: Los valores introducidos nos son validos")
        resultado = None
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")
        resultado = None
    return resultado