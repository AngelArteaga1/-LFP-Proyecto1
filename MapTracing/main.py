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
            Rutas = analizador.GetRutas()
            Estaciones = analizador.GetEstaciones()
            print('Ingrese la estación inicio: ')
            inicio = input()
            print('Ingrese la estación final: ')
            final = input()
            NombreMapa = analizador.GetNombreMapa()
            GraficarRuta(inicio, final, Rutas, Estaciones, NombreMapa)
        input()
    # END

    def GraficarMapa(self):
        global analizador
        if analizador == None:
            print('Porfavor ingrese la ruta del archivo primero.')
        else:
            Rutas = analizador.GetRutas()
            Estaciones = analizador.GetEstaciones()
            print('Ingrese la estación inicio: ')
            inicio = input()
            print('Ingrese la estación final: ')
            final = input()
            NombreMapa = analizador.GetNombreMapa()
            GraficarMapa(inicio, final, Rutas, Estaciones, NombreMapa)
        input()
    # END

    def quit(self):
        print("Gracias por usar MapTracing")
        sys.exit(0)
    # END

#Variables Globales
EncontroRuta = True
def EncontrarRuta(Rutas, Estaciones, Inicio, Fin):
    global EncontroRuta
    cerradas = []
    for i in Estaciones:
        if i.getestado() == False:
            cerradas.append((i.getnombre()).lower())
    LE = []
    LV = []
    Ordenar = []
    encontrado = False
    RutaAuxiliar = None
    EstacionesVistas = []
    RutaInicial = Ruta('rutainicial', 0, 'cero', Inicio)
    LE.append(RutaInicial)
    EstacionesVistas.append(Inicio)
    while (encontrado != True):
        Ordenar = []
        if len(LE) == 0:
            print('No se encontró una ruta adecuada :(')
            encontrado = True
            EncontroRuta = False
        if encontrado == False:
            RutaAuxiliar = LE[0]
            if (RutaAuxiliar.getfin()).lower() == Fin.lower():
                encontrado = True
                EncontroRuta = True
            LE.pop(0)
            for i in Rutas:
                if (i.getinicio()).lower() == (RutaAuxiliar.getfin()).lower():
                    Ordenar.append(i)
            if len(Ordenar) !=0:
                for numPasada in range(len(Ordenar) - 1, 0, -1):
                    for i in range(numPasada):
                        numero1 = float(Ordenar[i].getpeso())
                        numero2 = float(Ordenar[i + 1].getpeso())
                        if numero1 > numero2:
                            temp = Ordenar[i]
                            Ordenar[i] = Ordenar[i + 1]
                            Ordenar[i + 1] = temp
            if len(Ordenar) != 0:
                LV.append(RutaAuxiliar)
            else:
                if (RutaAuxiliar.getfin()).lower() == Fin.lower():
                    LV.append(RutaAuxiliar)
            for i in Ordenar:
                if i.getfin() in cerradas:
                    Ordenar.remove(i)
            for i in Ordenar:
                if (i.getfin()).lower() in EstacionesVistas:
                    Ordenar.remove(i)
            Ordenar = Ordenar[::-1]
            for i in Ordenar:
                LE.insert(0,i)
            EstacionesVistas.append(RutaAuxiliar.getfin())
    return LV
    # END

def GraficarRuta(Inicio, Fin, Rutas, Estaciones, NombreMapa):
    if NombreMapa == '':
        NombreMapa = 'Diagrama de Rutas'
    InicioEncontrado = False
    FinEncontrado = False
    for i in Estaciones:
        if (i.getnombre()).lower() == Inicio.lower():
            InicioEncontrado = True
        if (i.getnombre()).lower() == Fin.lower():
            FinEncontrado = True
    if InicioEncontrado == True and FinEncontrado == True:
        cerradas = []
        for i in Estaciones:
            if i.getestado() == False:
                cerradas.append((i.getnombre()).lower())
        if Inicio.lower() in cerradas:
            print('La estacion de inicio se encuentra cerrada')
        elif Fin.lower() in cerradas:
            print('La estacion final se encuentra cerrada')
        elif Inicio.lower() == Fin.lower():
            print('La estacion inicio es la misma que la final')
            file = open('GraficaRuta.dot', 'w', encoding="cp437", errors='ignore')
            file.write('digraph Grafica{\n')
            file.write('node[style=filled]\n')
            for i in Estaciones:
                if Inicio.lower() == (i.getnombre()).lower():
                    estacion = i
            nombre = estacion.getnombre()
            color = estacion.getcolor()
            if estacion.getestado() == True:
                estado = 'Disponible'
            else:
                estado = 'Cerrada'
            file.write(nombre + '[label = "' + str(estacion.getnombre()) + '\n' + estado + '", fillcolor = "' + color + '"]\n')
            file.write('}')
            file.close()
            print('Grafica de rutas generada exitosamente!')
        else:
            rutas = EncontrarRuta(Rutas, Estaciones, Inicio, Fin)
            if len(rutas) != 0:
                rutas.pop(0)
            if len(rutas) != 0:
                NombreEstaciones = []
                for i in rutas:
                    NombreEstaciones.append((i.getinicio()).lower())
                    NombreEstaciones.append((i.getfin()).lower())
                EstacionesReales = []
                for i in Estaciones:
                    if (i.getnombre()).lower() in NombreEstaciones:
                        EstacionesReales.append(i)
                file = open('GraficaRuta.dot', 'w', encoding="cp437", errors='ignore')
                file.write('digraph Grafica{\n')
                file.write('node[style=filled]\n')
                for i in EstacionesReales:
                    nombre = str(i.getnombre())
                    nombre = nombre.lower()
                    color = str(i.getcolor())
                    if i.getestado() == True:
                        Estado = 'Disponible'
                    else:
                        Estado = 'Cerrada'
                    file.write(nombre + '[label = "' + str(i.getnombre()) + '\n' + Estado + '", fillcolor = "' + color + '"]\n')
                file.write('rankdir="LR";\nlabelloc="t";\nlabel="' + NombreMapa + '";\nfontsize=24;\n')
                for i in rutas:
                    inicio = str(i.getinicio())
                    inicio = inicio.lower()
                    fin = str(i.getfin())
                    fin = fin.lower()
                    nombre = str(i.getnombre())
                    nombre = nombre.lower()
                    peso = str(i.getpeso())
                    file.write(inicio + '->' + fin + '[style = "bold", color = "#5D25FF", label = "' + nombre + '\n' + peso + '"]\n')
                file.write('}')
                file.close()
                print('Grafica de rutas generada exitosamente!')
    elif InicioEncontrado == False:
        print('La estacion inicial no existe :C')
    elif FinEncontrado == False:
        print('La estacion final no existe :C')
# END

def GraficarMapa(Inicio, Fin, Rutas, Estaciones, NombreMapa):
    if NombreMapa == '':
        NombreMapa = 'Diagrama del Mapa'
    InicioEncontrado = False
    FinEncontrado = False
    for i in Estaciones:
        if (i.getnombre()).lower() == Inicio.lower():
            InicioEncontrado = True
        if (i.getnombre()).lower() == Fin.lower():
            FinEncontrado = True
    if InicioEncontrado == True and FinEncontrado == True:
        cerradas = []
        for i in Estaciones:
            if i.getestado() == False:
                cerradas.append((i.getnombre()).lower())
        if Inicio.lower() in cerradas:
            print('La estacion de inicio se encuentra cerrada')
        elif Fin.lower() in cerradas:
            print('La estacion final se encuentra cerrada')
        else:
            rutas = EncontrarRuta(Rutas, Estaciones, Inicio, Fin)
            if len(rutas) != 0:
                rutas.pop(0)
            file = open('GraficaMapa.dot', 'w', encoding="cp437", errors='ignore')
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
                if i in rutas:
                    file.write(inicio + '->' + fin + '[style = "bold", color = "#5D25FF", label = "' + nombre + '\n' + peso + '"]\n')
                else:
                    file.write(inicio + '->' + fin + '[label = "' + nombre + '\n' + peso + '"]\n')
            file.write('}')
            file.close()
            print('Grafica del mapa generada exitosamente!')
    elif InicioEncontrado == False:
        print('La estacion inicial no existe :C')
    elif FinEncontrado == False:
        print('La estacion final no existe :C')
# END

'''******************************MAIN**********************************'''
if __name__ == '__main__':
    menu = Menu()
    menu.run()
# END
