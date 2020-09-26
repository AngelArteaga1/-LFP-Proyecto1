class Ruta:

    def __init__(self, direccion):
        self.direccion = direccion


    '''******************************FUNCION_LEER_ARCHIVO**********************************'''
    def LeerArchivo(self):
        leido = False
        if ".txt" in self.direccion:
            try:
                archivo = open(self.direccion, "r")
                print('leido')
                leido = True
            except:
                print("El archivo ingresado es incorrecto.\nPresione cualquier tecla para continuar")
                input()
            archivo.close()
        else:
            print("El archivo no es .txt o es incorrecto.\nPresione cualquier tecla para continuar")
            input()
        '''if leido == True:
            lineas = Manipulacion(direccion)
            Agrupacion(lineas)'''
    # END

