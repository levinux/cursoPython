class Ejemplo:
    def __init__(self, numero):
        self.numero = numero

class Animal:
    def __init__(self, nombre=""):
        self.nombre = nombre
    
    def camina(self):
        print("El animal {} esta caminando".format(self.nombre))


class Perro(Animal):
    def __init__(self, nombre=""):
        super().__init__(nombre)

    def guau(self):
        print("El perro {} esta ladrando...".format(self.nombre))
        self.__persigueSuCola()

    def __persigueSuCola(self):
        print("Mientras persigue su cola")


