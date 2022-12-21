from calculos import *

if "__name__" == "__main__":
    ejercicio = int(input("Elija el ejercicio: "))
    if ejercicio == 1:
       print( "{} + {} = {}".format(a, b, suma(a, b) ) )
       print( "{} - {} = {}".format(b, d, resta(b, d) ) )
       print( "{} * {} = {}".format(b, b, multiplicacion(b, b) ) )
       print( "{} / {} = {}".format(a, c, division(a, c) ) ) 
    