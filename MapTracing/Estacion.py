class Estacion:

    def __init__(self, nombre, estado, color):
        self.nombre = nombre
        self.estado = estado
        self.color = color

    '''******************************FUNCIONES/GET/SET**********************************'''
    def getnombre(self):
        return self.nombre
    # END
    def getestado(self):
        return self.estado
    # END
    def getcolor(self):
        return self.color
    # END
    def setnombre(self, nombre):
        self.nombre = nombre
    # END
    def setestado(self, estado):
        self.estado = estado
    # END
    def setcolor(self, color):
        self.color = color
    # END