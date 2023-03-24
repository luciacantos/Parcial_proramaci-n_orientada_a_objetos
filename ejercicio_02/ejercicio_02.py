class Animal:
    def __init__(self, edad, especie):
        self.edad = edad
        self.especie = especie

class Mamífero(Animal):
    def__init__(self, edad, especie, pelaje):
        super().__init__(edad, especie)
        self.pelaje = pelaje
    