class Libro:
    def __init__(self,título,autor,editorial,páginas,año,):
        self.título = título
        self.autor = autor
        self.editorial = editorial
        self.páginas = páginas
        self.año = año

    def getTítulo(self):
        return self.título
    def getAutor(self):
        return self.autor
    def getEditorial(self):
        return self.editorial
    def getPáginas(self):
        return self.páginas
    def getAño(self):
        return self.año

    def descripción(self):
        print("Título: "+ self.getTítulo() + "Autor: " + self.getAutor() + "Editorial: " + self.getEditorial() + "Páginas: " + str(self.getPáginas()) + "Año: " + str(self.getAño()))

    título = raw_input("Introduce el nombre: ") #cadena caracteres
    autor = raw_input("Introduce el autor:") #cadena caracteres
    editorial = raw_input("Introcuce la editorial: ") #cadena caracteres
