class Ruta:

    def __init__(self, nombre, peso, inicio, fin):
        self.nombre = nombre
        self.peso = peso
        self.inicio = inicio
        self.fin = fin

    '''******************************FUNCIONES/GET/SET**********************************'''
    def getnombre(self):
        return self.nombre
    # END
    def getpeso(self):
        return self.peso
    # END
    def getinicio(self):
        return self.inicio
    # END
    def getfin(self):
        return self.fin
    # END
    def setnombre(self, nombre):
        self.nombre = nombre
    # END
    def setpeso(self, peso):
        self.peso = peso
    # END
    def setinicio(self, inicio):
        self.inicio = inicio
    # END
    def setfin(self, fin):
        self.fin = fin
    # END