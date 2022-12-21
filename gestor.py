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