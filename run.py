
if "__name__" == "__main__":
    ejercicio = int(input("Elija el ejercicio: "))
    if ejercicio == 1:
        from calculos import *
        print( "{} + {} = {}".format(a, b, suma(a, b) ) )
        print( "{} - {} = {}".format(b, d, resta(b, d) ) )
        print( "{} * {} = {}".format(b, b, multiplicacion(b, b) ) )
        print( "{} / {} = {}".format(a, c, division(a, c) ) ) 
    elif ejercicio == 2:
        from contador import *
        print(contador)
        with open("contador.txt", "w") as f:
            f.write(str(contador))
    elif ejercicio == 3:
        from gestor import *
        gestor = Gestor()
        caballero= Personaje("Caballero", 4,2, 4, 2)
        gestor.agregar_personaje(caballero)
        arquero= Personaje("Arquero", 2,4,1,8)
        gestor.agregar_personaje(arquero)
        guerrero= Personaje("Guerrero", 2,4,2,4)
        gestor.agregar_personaje(guerrero)
        gestor.mostrar_personaje()
        gestor.borrar_personaje("Arquero")
        gestor.mostrar_personaje()
        gestor.guardar()
    elif ejercicio == 4:
        from reloj import *
        print(hora_actual.strftime("%H:%M:%S"))