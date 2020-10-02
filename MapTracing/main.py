# This is my own Python script
# Imports
import sys
from Analizador import Analizador
from Ruta import Ruta
from Estacion import Estacion

# VARIABLES GLOBALES
analizador = None

'''******************************MENU**********************************'''
class Menu:

    def __init__(self):
        self.elecciones = {
            "1": self.CargarArchivo,
            "2": self.GraficarRuta,
            "3": self.GraficarMapa,
            "4": self.quit
        }
    # END

    def mostrar_menu(self):
        print("""
        ************** PROYECTO 1 **************
        | Lenguajes Formales y de Programación |
        | Sección: A-, Canet: 201901816        |
        | Angel Oswaldo Arteaga García         |
        ****************************************

        *******+*** MAP TRACING MENU **+********
        1. Cargar Archivo
        2. Graficar Ruta
        3. Graficar Mapa
        4. Salir
        """)
    # END

    def run(self):
        while True:
            self.mostrar_menu()
            eleccion = input(">>Ingrese una opción:")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
            else:
                print("No es una elección válida".format(eleccion))
    # END

    def CargarArchivo(self):
        print("Porfavor intruduzca la ubicación del archivo:")
        global analizador
        analizador = Analizador(input())
        analizador.LeerArchivo()
        input()
    # END

    def GraficarRuta(self):
        global analizador
        if analizador == None:
            print('Porfavor ingrese la ruta del archivo primero.')
        else:
            if analizador.IsCorrecta():
                Rutas = analizador.GetRutas()
                Estaciones = analizador.GetEstaciones()
                for i in Rutas:
                    print('**********RUTA**********')
                    print('Nombre: ' + i.getnombre())
                    print('Peso: ' + i.getpeso())
                    print('inicio: ' + i.getinicio())
                    print('fin: ' + i.getfin())
                for i in Estaciones:
                    print('********ESTACION********')
                    print('Nombre: ' + i.getnombre())
                    if i.getestado() == True:
                        print('Estado: disponible')
                    else:
                        print('Estado: cerrada')
                    print('color: ' + i.getcolor())
                print('Nombre del Mapa: ' + analizador.GetNombreMapa())
                GraficarRuta()
            else:
                print('Se han encontrado errores en su archivo...')
                print('Porfavor corrigalos he intente de nuevo')
        input()
    # END

    def GraficarMapa(self):
        global analizador
        if analizador == None:
            print('Porfavor ingrese la ruta del archivo primero.')
        else:
            if analizador.IsCorrecta():
                Rutas = analizador.GetRutas()
                Estaciones = analizador.GetEstaciones()
                for i in Rutas:
                    print('**********RUTA**********')
                    print('Nombre: ' + i.getnombre())
                    print('Peso: ' + i.getpeso())
                    print('inicio: ' + i.getinicio())
                    print('fin: ' + i.getfin())
                for i in Estaciones:
                    print('********ESTACION********')
                    print('Nombre: ' + i.getnombre())
                    if i.getestado() == True:
                        print('Estado: disponible')
                    else:
                        print('Estado: cerrada')
                    print('color: ' + i.getcolor())
                print('Nombre del Mapa: ' + analizador.GetNombreMapa())
                NombreMapa = analizador.GetNombreMapa()
                if NombreMapa != '':
                    NombreMapa = analizador.GetNombreMapa()
                else:
                    NombreMapa = 'Diagrama Del Mapa'
                GraficarMapa(Rutas, Estaciones, NombreMapa)
            else:
                print('Se han encontrado errores en su archivo...')
                print('Porfavor corrigalos he intente de nuevo')
        input()
    # END

    def quit(self):
        print("Gracias por usar MapTracing")
        sys.exit(0)
    # END

def GraficarRuta():
    print('Graficando ruta...')
# END

def GraficarMapa(Rutas, Estaciones, NombreMapa):
    file = open('GraficaMapa.dot', 'w')
    file.write('digraph Grafica{\n')
    file.write('node[style=filled]\n')
    for i in Estaciones:
        nombre = str(i.getnombre())
        nombre = nombre.lower()
        color = str(i.getcolor())
        if i.getestado() == True:
            Estado = 'Disponible'
        else:
            Estado = 'Cerrada'
        file.write(nombre + '[label = "'+ str(i.getnombre()) + '\n' + Estado + '", fillcolor = "'+ color + '"]\n')
    file.write('rankdir="LR";\nlabelloc="t";\nlabel="'+ NombreMapa +'";\nfontsize=24;\n')
    for i in Rutas:
        inicio = str(i.getinicio())
        inicio = inicio.lower()
        fin = str(i.getfin())
        fin = fin.lower()
        nombre = str(i.getnombre())
        nombre = nombre.lower()
        peso = str(i.getpeso())
        file.write(inicio + '->' + fin + '[label = "' + nombre + '\n' + peso + '"]\n')
    file.write('}')
    file.close()
    print('Graficando mapa...')
# END

'''******************************MAIN**********************************'''
if __name__ == '__main__':
    menu = Menu()
    menu.run()
# END
