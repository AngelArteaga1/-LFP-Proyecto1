# This is my own Python script
# Imports
import sys
from Ruta import Ruta


'''******************************MENU**********************************'''
class Menu:

    def __init__(self):
        self.elecciones = {
            "1": self.CargarArchivo,
            "2": self.GraficarRuta,
            "3": self.GraficarMapa,
            "4": self.quit
        }

    def mostrar_menu(self):
        print("""
        ************** PROYECTO 1 **************
        | Lenguajes Formales y de Programación |
        | Sección: A-, Canet: 201901816        |
        | Angel Oswaldo Arteaga García         |
        ****************************************

        ********** MAP TRACING MENU **********
        1. Cargar Archivo
        2. Graficar Ruta
        3. Graficar Mapa
        4. Salir
        """)

    def run(self):
        while True:
            self.mostrar_menu()
            eleccion = input(">>Ingrese una opción:")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
            else:
                print("No es una elección válida".format(eleccion))

    def CargarArchivo(self):
        print("Porfavor intruduzca la ubicación del archivo:")
        ruta = Ruta(input())
        ruta.LeerArchivo()
        input()

    def GraficarRuta(self):
        print('Graficar Ruta')

    def GraficarMapa(self):
        print('Graficar Mapa')

    def quit(self):
        print("Gracias por usar STACK CALC")
        sys.exit(0)

'''******************************MAIN**********************************'''
if __name__ == '__main__':
    menu = Menu()
    menu.run()

