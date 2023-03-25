
class Animal():
    def __init__(self, name):
        self.name = name

class Mamifero(Animal):
    def __init__(self, name):
        Animal.__init__(self,name)

class Oviparo(Animal):
    def __init__(self, name):
        Animal.__init__(self,name)

class Gato(Mamifero):
    def __init__(self, name):
        Mamifero.__init__(self,name)

class Ornitorrinco(Mamifero,Oviparp):
    def __init__(self, name):
        Mamifero.__init__(self,name)
        Oviparo.__init__(self,name)

class Pollo(Oviparo):
    def __init__(self, name):
        Oviparo.__init__(self,name)

'''''''''''''''''''''''''''
opción con super()

class Animal:
    def __init__(self, especie,edad):
        self.especie = especie
        self.edad = edad

class Mamifero(Animal):
    def __init__(self, especie, edad, tipo):
        super().__init__(especie,edad)
        self.tipo = tipo

class Oviparo(Animal):
    def __init__(self, especie, edad, tipo):
        super().__init__(especie,edad)
        self.tipo = tipo

class Gato(Mamifero):
    def __init__(self, especie, edad, tipo, nombre):
        super().__init__(especie,edad,tipo)
        self.nombre = nombre

class Ornitorrinco(Mamifero,Oviparo):
    def __init__(self, especie, edad, tipo, nombre):
        super().__init__(especie,edad,tipo)
        self.nombre = nombre

class Pollo(Oviparo):
    def __init__(self, especie, edad, tipo, nombre):
        super().__init__(especie,edad,tipo)
        self.nombre = nombre
'''''''''''''''''''''
