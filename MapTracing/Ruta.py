import re
class Ruta:

    def __init__(self, direccion):
        self.direccion = direccion


    '''******************************FUNCION_LEER_ARCHIVO**********************************'''
    def LeerArchivo(self):
        leido = False
        rutatxt = self.direccion
        if ".txt" in rutatxt:
            try:
                archivo = open(rutatxt, "r")
                leido = True
            except:
                print("El archivo ingresado es incorrecto.\nPresione cualquier tecla para continuar")
                input()
            archivo.close()
        else:
            print("El archivo no es .txt o es incorrecto.\nPresione cualquier tecla para continuar")
            input()
        if leido == True:
            archivo = open(rutatxt, encoding="cp437", errors='ignore')
            lineas = archivo.readlines()
            archivo.close()
            argumento = ''
            for i in lineas:
                argumento = argumento+i
            AnalisisLexico(lineas)
    # END

# VARIABLES GLOBALES
NoTabla = 0
NoError = 1
Error = False
especiales = ["@", "#", "_"]
S = 0 # ESTADOS DE AUTOMATA


def GraficarErrores(fila, columna, simbolo, descripcion, error):
    global NoError
    global NoTabla
    print('Fila: ' + str(fila) + ' columna: ' + str(columna) + ' simbolo: ' + simbolo + ' error:' + str(error))
    if NoTabla == 0:
        file = open("TablaErrores.csv", "w")
        file.write('No.,Fila,Colunma,Caracter,Descripcion\n')
        file.close()
        NoTabla = 1
    if NoTabla != 0:
        file = open("TablaErrores.csv", "a")
        file.write(str(NoError) + ',' + str(fila) + ',' + str(columna) + ',' +simbolo+ ',' + descripcion + '\n')
        file.close()
    NoError = NoError + 1
    # END

def GraficarToken(lexema, fila, columna, token):
    print('Lexema: ' + lexema + ' fila: ' + fila + ' columna: ' + columna + ' Token: ' + token)
    # END

def AnalisisLexico(lineas):
    temporal = ''
    contador = 0
    # Quitarle los tabuladores a cada linea
    for i in lineas:
        lineas[contador] = re.sub('[\t]', ' ', lineas[contador])
        lineas[contador] = re.sub('[\n]', '', lineas[contador])
        contador = contador + 1
    # Enviar cada linea a su analisis
    contador = 1
    for i in lineas:
        AutomataGeneral1(i, contador)
        contador = contador + 1
    print('Estado: ' + str(S))
    # END

def AutomataGeneral1(linea, fila):
    global S
    global Error
    columna = 1
    for i in linea:
        # ***********************ERRORES**************************
        # ERROR -1
        if S == -1:
            if i == 'r':
                S = 2
            elif i == 'u':
                S = 3
            elif i == 't':
                S = 4
            elif i == 'a':
                S = 5
            elif i == '>':
                S = 6
            elif i == '<':
                S = 7
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "ruta"', S)
        # ERROR -2
        elif S == -2:
            if i == 'n':
                S = 8
            elif i == 'o':
                S = 9
            elif i == 'm':
                S = 10
            elif i == 'b':
                S = 11
            elif i == 'r':
                S = 12
            elif i == 'e':
                S = 13
            elif i == '>':
                S = 14
            elif i == '<':
                S = 16
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ERROR -3
        elif S == -3:
            if i == 'p':
                S = 26
            elif i == 'e':
                S = 27
            elif i == 's':
                S = 28
            elif i == 'o':
                S = 29
            elif i == '>':
                S = 30
            elif i == '<':
                S = 33
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "peso"', S)
        # ERROR -4
        elif S == -4:
            if i == 'i':
                S = 41
            elif i == 'n':
                S = 42
            elif i == 'i':
                S = 43
            elif i == 'c':
                S = 44
            elif i == 'i':
                S = 45
            elif i == 'o':
                S = 46
            elif i == '>':
                S = 47
            elif i == '<':
                S = 49
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ERROR -5
        elif S == -5:
            if i == 'f':
                S = 59
            elif i == 'i':
                S = 60
            elif i == 'n':
                S = 61
            elif i == '>':
                S = 62
            elif i == '<':
                S = 64
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "fin"', S)
        # ERROR -6
        elif S == -6:
            if i == '/':
                S = 17
            elif i == 'n':
                S = 18
            elif i == 'o':
                S = 19
            elif i == 'm':
                S = 20
            elif i == 'b':
                S = 21
            elif i == 'r':
                S = 22
            elif i == 'e':
                S = 23
            elif i == '>':
                S = 24
            elif i == '<':
                S = 7
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ERROR -7
        elif S == -7:
            if i == '/':
                S = 37
            elif i == 'p':
                S = 38
            elif i == 'e':
                S = 39
            elif i == 's':
                S = 40
            elif i == 'o':
                S = 41
            elif i == '>':
                S = 42
            elif i == '<':
                S = 7
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "peso"', S)
        # ERROR -8
        elif S == -8:
            if i == '/':
                S = 50
            elif i == 'i':
                S = 51
            elif i == 'n':
                S = 52
            elif i == 'i':
                S = 53
            elif i == 'c':
                S = 54
            elif i == 'i':
                S = 55
            elif i == 'o':
                S = 56
            elif i == '>':
                S = 57
            elif i == '<':
                S = 7
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ERROR -9
        elif S == -9:
            if i == '/':
                S = 65
            elif i == 'f':
                S = 66
            elif i == 'i':
                S = 67
            elif i == 'n':
                S = 68
            elif i == '>':
                S = 69
            elif i == '<':
                S = 7
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "fin"', S)
        # ERROR -10
        elif S == -10:
            if i == '/':
                S = 71
            elif i == 'r':
                S = 72
            elif i == 'u':
                S = 73
            elif i == 't':
                S = 74
            elif i == 'a':
                S = 75
            elif i == '>':
                S = 0
            elif i == '<':
                S = 1
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "ruta"', S)
        # ERROR -11
        elif S == -11:
            if i == 'e':
                S = 77
            elif i == 's':
                S = 78
            elif i == 't':
                S = 79
            elif i == 'a':
                S = 80
            elif i == 'c':
                S = 81
            elif i == 'i':
                S = 82
            elif i == 'o':
                S = 83
            elif i == 'n':
                S = 84
            elif i == '>':
                S = 85
            elif i == '<':
                S = 86
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ERROR -12
        elif S == -12:
            if i == 'n':
                S = 87
            elif i == 'o':
                S = 88
            elif i == 'm':
                S = 89
            elif i == 'b':
                S = 90
            elif i == 'r':
                S = 91
            elif i == 'e':
                S = 92
            elif i == '>':
                S = 93
            elif i == '<':
                S = 95
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ERROR -13
        elif S == -13:
            if i == 'e':
                S = 104
            elif i == 's':
                S = 105
            elif i == 't':
                S = 106
            elif i == 'a':
                S = 107
            elif i == 'd':
                S = 108
            elif i == 'o':
                S = 109
            elif i == '>':
                S = 110
            elif i == '<':
                S = 121
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ERROR -14
        elif S == -14:
            if i == 'c':
                S = 137
            elif i == 'o':
                S = 138
            elif i == 'l':
                S = 139
            elif i == 'o':
                S = 140
            elif i == 'r':
                S = 141
            elif i == '>':
                S = 142
            elif i == '<':
                S = 144
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ERROR -15
        elif S == -15:
            if i == '/':
                S = 97
            elif i == 'n':
                S = 98
            elif i == 'o':
                S = 99
            elif i == 'm':
                S = 100
            elif i == 'b':
                S = 101
            elif i == 'r':
                S = 102
            elif i == 'e':
                S = 103
            elif i == '>':
                S = 104
            elif i == '<':
                S = 86
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ERROR -16
        elif S == -16:
            if i == '/':
                S = 122
            elif i == 'e':
                S = 123
            elif i == 's':
                S = 124
            elif i == 't':
                S = 125
            elif i == 'a':
                S = 126
            elif i == 'd':
                S = 127
            elif i == 'o':
                S = 128
            elif i == '>':
                S = 129
            elif i == '<':
                S = 86
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ERROR -17
        elif S == -17:
            if i == '/':
                S = 145
            elif i == 'c':
                S = 146
            elif i == 'o':
                S = 147
            elif i == 'l':
                S = 148
            elif i == 'o':
                S = 149
            elif i == 'r':
                S = 150
            elif i == '>':
                S = 100
            elif i == '<':
                S = 86
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ERROR -18
        elif S == -18:
            if i == '/':
                S = 151
            elif i == 'e':
                S = 152
            elif i == 's':
                S = 153
            elif i == 't':
                S = 154
            elif i == 'a':
                S = 155
            elif i == 'c':
                S = 156
            elif i == 'i':
                S = 157
            elif i == 'o':
                S = 158
            elif i == 'n':
                S = 159
            elif i == '>':
                S = 0
            elif i == '<':
                S = 1
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ERROR -19
        elif S == -19:
            if i == 'n':
                S = 160
            elif i == 'o':
                S = 161
            elif i == 'm':
                S = 162
            elif i == 'b':
                S = 163
            elif i == 'r':
                S = 164
            elif i == 'e':
                S = 165
            elif i == '>':
                S = 166
            elif i == '<':
                S = 168
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ERROR -20
        elif S == -20:
            if i == '/':
                S = 168
            elif i == 'n':
                S = 169
            elif i == 'o':
                S = 170
            elif i == 'm':
                S = 171
            elif i == 'b':
                S = 172
            elif i == 'r':
                S = 173
            elif i == 'e':
                S = 174
            elif i == '>':
                S = 0
            elif i == '<':
                S = 1
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ERROR -21
        elif S == -21:
            if i == 'd':
                S = 111
            elif i == 'i':
                S = 112
            elif i == 's':
                S = 113
            elif i == 'p':
                S = 114
            elif i == 'o':
                S = 115
            elif i == 'n':
                S = 116
            elif i == 'i':
                S = 117
            elif i == 'b':
                S = 118
            elif i == 'l':
                S = 119
            elif i == 'e':
                S = 120
            elif i == '<':
                S = 121
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ERROR -22
        elif S == -22:
            if i == 'c':
                S = 130
            elif i == 'e':
                S = 131
            elif i == 'r':
                S = 132
            elif i == 'a':
                S = 134
            elif i == 'd':
                S = 135
            elif i == '<':
                S = 121
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # **************************RUTA**************************
        # ESTADO 0
        elif S == 0:
            if i == '<':
                S = 1
            elif i == ' ':
                S = 0
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 1
        elif S == 1:
            if i == 'r':
                S = 2
            elif i == 'e':
                S = 77
            elif i == 'n':
                S = 160
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 2
        elif S == 2:
            if i == 'u':
                S = 3
            else:
                S = -1
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "ruta"', S)
        # ESTADO 3
        elif S == 3:
            if i == 't':
                S = 4
            else:
                S = -1
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "ruta"', S)
        # ESTADO 4
        elif S == 4:
            if i == 'a':
                S = 5
            else:
                S = -1
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "ruta"', S)
        # ESTADO 5
        elif S == 5:
            if i == '>':
                S = 6
            elif i == ' ':
                S = 5
            else:
                S = -1
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "ruta"', S)
        # ESTADO 6
        elif S == 6:
            if i == '<':
                S = 7
            elif i == ' ':
                S = 6
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 7
        elif S == 7:
            if i == 'n':
                S = 8
            elif i == 'p':
                S = 26
            elif i == 'i':
                S = 41
            elif i == 'f':
                S = 59
            elif i == '/':
                S = 71
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 8
        elif S == 8:
            if i == 'o':
                S = 9
            else:
                S = -2
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 9
        elif S == 9:
            if i == 'm':
                S = 10
            else:
                S = -2
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 10
        elif S == 10:
            if i == 'b':
                S = 11
            else:
                S = -2
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 11
        elif S ==11:
            if i == 'r':
                S = 12
            else:
                S = -2
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 12
        elif S == 12:
            if i == 'e':
                S = 13
            else:
                S = -2
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 13
        elif S == 13:
            if i == '>':
                S = 14
            elif i == ' ':
                S = 13
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 14 / EXPRESION REGULAR
        elif S == 14:
            if i.isalpha():
                S = 15
            elif i == ' ':
                S = 14
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 15 / EXPRESION REGULAR
        elif S == 15:
            if i.isalnum() or i in especiales:
                S = 15
            elif i == '<':
                S = 16
            elif i ==' ':
                S = 15
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 16
        elif S == 16:
            if i == '/':
                S = 17
            else:
                S = -6
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 17
        elif S == 17:
            if i == 'n':
                S = 18
            else:
                S = -6
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 18
        elif S == 18:
            if i == 'o':
                S = 19
            else:
                S = -6
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 19
        elif S == 19:
            if i == 'm':
                S = 20
            else:
                S = -6
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 20
        elif S == 20:
            if i == 'b':
                S = 21
            else:
                S = -6
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 21
        elif S == 21:
            if i == 'r':
                S = 22
            else:
                S = -6
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 22
        elif S == 22:
            if i == 'e':
                S = 23
            else:
                S = -6
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 23
        elif S == 23:
            if i == '>':
                S = 24
            elif i ==' ':
                S = 23
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 24
        elif S == 24:
            if i == '<':
                S = 7
            elif i == ' ':
                S = 24
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 26
        elif S == 26:
            if i == 'e':
                S = 27
            else:
                S = -3
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "peso"', S)
        # ESTADO 27
        elif S == 27:
            if i == 's':
                S = 28
            else:
                S = -3
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "peso"', S)
        # ESTADO 28
        elif S == 28:
            if i == 'o':
                S = 29
            else:
                S = -3
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "peso"', S)
        # ESTADO 29
        elif S == 29:
            if i == '>':
                S = 30
            elif i == ' ':
                S = 29
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "peso"', S)
        # ESTADO 30 / EXPRESION REGULAR
        elif S == 30:
            if i.isdigit():
                S = 31
            elif i == ' ':
                S = 30
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 31 / EXPRESION REGULAR
        elif S == 31:
            if i.isdigit():
                S = 31
            elif i == '.':
                S = 32
            elif i == "<":
                S = 33
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 32 / EXPRESION REGULAR
        elif S == 32:
            if i.isdigit():
                S = 32
            elif i == '<':
                S = 33
            elif i == ' ':
                S = 32
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 33
        elif S == 33:
            if i == '/':
                S = 34
            else:
                S = -7
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "peso"', S)
        # ESTADO 34
        elif S == 34:
            if i == 'p':
                S = 35
            else:
                S = -7
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "peso"', S)
        # ESTADO 35
        elif S == 35:
            if i == 'e':
                S = 36
            else:
                S = -7
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "peso"', S)
        # ESTADO 36
        elif S == 36:
            if i == 's':
                S = 37
            else:
                S = -7
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "peso"', S)
        # ESTADO 37
        elif S == 37:
            if i == 'o':
                S = 38
            else:
                S = -7
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "peso"', S)
        # ESTADO 38
        elif S == 38:
            if i == '>':
                S = 39
            elif i == ' ':
                S = 38
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "peso"', S)
        # ESTADO 39
        elif S == 39:
            if i == '<':
                S = 7
            elif i == ' ':
                S = 39
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 41
        elif S == 41:
            if i == 'n':
                S = 42
            else:
                S = -4
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ESTADO 42
        elif S == 42:
            if i == 'i':
                S = 43
            else:
                S = -4
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ESTADO 43
        elif S == 43:
            if i == 'c':
                S = 44
            else:
                S = -4
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ESTADO 44
        elif S == 44:
            if i == 'i':
                S = 45
            else:
                S = -4
                Error = True
                GraficarErrores(fila, columna, i, 'desconocida', S)
        # ESTADO 45
        elif S == 45:
            if i == 'o':
                S = 46
            else:
                S = -4
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ESTADO 46
        elif S == 46:
            if i == '>':
                S = 47
            elif i == ' ':
                S = 46
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ESTADO 47 / EXPRESION REGULAR
        elif S == 47:
            if i.isalpha():
                S = 48
            elif i == ' ':
                S = 47
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 48 / EXPRESION REGULAR
        elif S == 48:
            if i.isalnum() or i in especiales:
                S = 48
            elif i == '<':
                S = 49
            elif i == ' ':
                S = 48
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 49
        elif S == 49:
            if i == '/':
                S = 50
            else:
                S = -8
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ESTADO 50
        elif S == 50:
            if i == 'i':
                S = 51
            else:
                S = -8
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ESTADO 51
        elif S == 51:
            if i == 'n':
                S = 52
            else:
                S = -8
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ESTADO 52
        elif S == 52:
            if i == 'i':
                S = 53
            else:
                S = -8
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ESTADO 53
        elif S == 53:
            if i == 'c':
                S = 54
            else:
                S = -8
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ESTADO 54
        elif S == 54:
            if i == 'i':
                S = 55
            else:
                S = -8
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ESTADO 55
        elif S == 55:
            if i == 'o':
                S = 56
            else:
                S = -8
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ESTADO 56
        elif S == 56:
            if i == '>':
                S = 57
            elif i == ' ':
                S = 56
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "inicio"', S)
        # ESTADO 57
        elif S == 57:
            if i == '<':
                S = 7
            elif i == ' ':
                S = 57
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 59
        elif S == 59:
            if i == 'i':
                S = 60
            else:
                S = -5
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "fin"', S)
        # ESTADO 60
        elif S == 60:
            if i == 'n':
                S = 61
            else:
                S = -5
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "fin"', S)
        # ESTADO 61
        elif S == 61:
            if i == '>':
                S = 62
            elif i == ' ':
                S = 61
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "fin"', S)
        # ESTADO 62 / EXPRESION REGULAR
        elif S == 62:
            if i.isalpha():
                S = 63
            elif i == ' ':
                S = 62
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 63 / EXPRESION REGULAR
        elif S == 63:
            if i.isalnum() or i in especiales:
                S = 63
            elif i == '<':
                S = 64
            elif i == ' ':
                S = 63
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 64
        elif S == 64:
            if i == '/':
                S = 65
            else:
                S = -9
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "fin"', S)
        # ESTADO 65
        elif S == 65:
            if i == 'f':
                S = 66
            else:
                S = -9
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "fin"', S)
        # ESTADO 66
        elif S == 66:
            if i == 'i':
                S = 67
            else:
                S = -9
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "fin"', S)
        # ESTADO 67
        elif S == 67:
            if i == 'n':
                S = 68
            else:
                S = -9
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "fin"', S)
        # ESTADO 68
        elif S == 68:
            if i == '>':
                S = 69
            elif i == ' ':
                S = 68
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "fin"', S)
        # ESTADO 69
        elif S == 69:
            if i == '<':
                S = 7
            elif i == ' ':
                S = 69
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 71
        elif S == 71:
            if i == 'r':
                S = 72
            else:
                S = -10
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "ruta"', S)
        # ESTADO 72
        elif S == 72:
            if i == 'u':
                S = 73
            else:
                S = -10
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "ruta"', S)
        # ESTADO 73
        elif S == 73:
            if i == 't':
                S = 74
            else:
                S = -10
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "ruta"', S)
        # ESTADO 74
        elif S == 74:
            if i == 'a':
                S = 75
            else:
                S = -10
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "ruta"', S)
        # ESTADO 75
        elif S == 75:
            if i == '>':
                S = 0
            elif i == ' ':
                S = 75
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "ruta"', S)
        # **************************ESTACION**************************
        # ESTADO 77
        elif S == 77:
            if i == 's':
                S = 78
            else:
                S = -11
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 78
        elif S == 78:
            if i == 't':
                S = 79
            else:
                S = -11
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 79
        elif S == 79:
            if i == 'a':
                S = 80
            else:
                S = -11
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 80
        elif S == 80:
            if i == 'c':
                S = 81
            else:
                S = -11
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 81
        elif S == 81:
            if i == 'i':
                S = 82
            else:
                S = -11
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 82
        elif S == 82:
            if i == 'o':
                S = 83
            else:
                S = -11
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 83
        elif S == 83:
            if i == 'n':
                S = 84
            else:
                S = -11
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 84
        elif S == 84:
            if i == '>':
                S = 85
            elif i == ' ':
                S = 84
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 85
        elif S == 85:
            if i == '<':
                S = 86
            elif i == ' ':
                S = 85
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 86
        elif S == 86:
            if i == 'n':
                S = 87
            elif i == 'e':
                S = 104
            elif i == 'c':
                S = 137
            elif i == '/':
                S = 151
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 87
        elif S == 87:
            if i == 'o':
                S = 88
            else:
                S = -12
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 88
        elif S == 88:
            if i == 'm':
                S = 89
            else:
                S = -12
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 89
        elif S == 89:
            if i == 'b':
                S = 90
            else:
                S = -12
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 90
        elif S == 90:
            if i == 'r':
                S = 91
            else:
                S = -12
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 91
        elif S == 91:
            if i == 'e':
                S = 92
            else:
                S = -12
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 92
        elif S == 92:
            if i == '>':
                S = 93
            elif i == ' ':
                S = 92
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 93 / EXPRESION REGULAR
        elif S == 93:
            if i.isalpha():
                S = 94
            elif i == ' ':
                S = 93
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 94 / EXPRESION REGULAR
        elif S == 94:
            if i.isalnum() or i in especiales:
                S = 94
            elif i == '<':
                S = 95
            elif i == ' ':
                S = 94
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 95
        elif S == 95:
            if i == '/':
                S = 96
            else:
                S = -15
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 96
        elif S == 96:
            if i == 'n':
                S = 97
            else:
                S = -15
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 97
        elif S == 97:
            if i == 'o':
                S = 98
            else:
                S = -15
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 98
        elif S == 98:
            if i == 'm':
                S = 99
            else:
                S = -15
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 99
        elif S == 99:
            if i == 'b':
                S = 100
            else:
                S = -15
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 100
        elif S == 100:
            if i == 'r':
                S = 101
            else:
                S = -15
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 101
        elif S == 101:
            if i == 'e':
                S = 102
            else:
                S = -15
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 102
        elif S == 102:
            if i == '>':
                S = 103
            elif i == ' ':
                S = 102
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 103
        elif S == 103:
            if i == '<':
                S = 86
            elif i == ' ':
                S = 103
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 104
        elif S == 104:
            if i == 's':
                S = 105
            else:
                S = -13
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 105
        elif S == 105:
            if i == 't':
                S = 106
            else:
                S = -13
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 106
        elif S == 106:
            if i == 'a':
                S = 107
            else:
                S = -13
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 107
        elif S == 107:
            if i == 'd':
                S = 108
            else:
                S = -13
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 108
        elif S == 108:
            if i == 'o':
                S = 109
            else:
                S = -13
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 109
        elif S == 109:
            if i == '>':
                S = 110
            elif i == ' ':
                S = 109
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 110
        elif S == 110:
            if i == 'd':
                S = 111
            elif i == 'c':
                S = 130
            elif i == ' ':
                S = 110
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 111
        elif S == 111:
            if i == 'i':
                S = 112
            else:
                S = -21
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 112
        elif S == 112:
            if i == 's':
                S = 113
            else:
                S = -21
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 113
        elif S == 113:
            if i == 'p':
                S = 114
            else:
                S = -21
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 114
        elif S == 114:
            if i == 'o':
                S = 115
            else:
                S = -21
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 115
        elif S == 115:
            if i == 'n':
                S = 116
            else:
                S = -21
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 116
        elif S == 116:
            if i == 'i':
                S = 117
            else:
                S = -21
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 117
        elif S == 117:
            if i == 'b':
                S = 118
            else:
                S = -21
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 118
        elif S == 118:
            if i == 'l':
                S = 119
            else:
                S = -21
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 119
        elif S == 119:
            if i == 'e':
                S = 120
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 120
        elif S == 120:
            if i == '<':
                S = 121
            elif i == ' ':
                S = 120
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 121
        elif S == 121:
            if i == '/':
                S = 122
            else:
                S = -16
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 122
        elif S == 122:
            if i == 'e':
                S = 123
            else:
                S = -16
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 123
        elif S == 123:
            if i == 's':
                S = 124
            else:
                S = -16
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 124
        elif S == 124:
            if i == 't':
                S = 125
            else:
                S = -16
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 125
        elif S == 125:
            if i == 'a':
                S = 126
            else:
                S = -16
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 126
        elif S == 126:
            if i == 'd':
                S = 127
            else:
                S = -16
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 127
        elif S == 127:
            if i == 'o':
                S = 128
            else:
                S = -16
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 128
        elif S == 128:
            if i == '>':
                S = 129
            elif i == ' ':
                S = 128
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estado"', S)
        # ESTADO 129
        elif S == 129:
            if i == '<':
                S = 86
            elif i == ' ':
                S = 129
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 130
        elif S == 130:
            if i == 'e':
                S = 131
            else:
                S = -22
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 131
        elif S == 131:
            if i == 'r':
                S = 132
            else:
                S = -22
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 132
        elif S == 132:
            if i == 'r':
                S = 133
            else:
                S = -22
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 133
        elif S == 133:
            if i == 'a':
                S = 134
            else:
                S = -22
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 134
        elif S == 134:
            if i == 'd':
                S = 135
            else:
                S = -22
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 135
        elif S == 135:
            if i == 'a':
                S = 136
            else:
                S = -22
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 136
        elif S == 136:
            if i == '<':
                S = 121
            elif i == ' ':
                S = 136
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 137
        elif S == 137:
            if i == 'o':
                S = 138
            else:
                S = -14
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ESTADO 138
        elif S == 138:
            if i == 'l':
                S = 139
            else:
                S = -14
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ESTADO 139
        elif S == 139:
            if i == 'o':
                S = 140
            else:
                S = -14
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ESTADO 140
        elif S == 140:
            if i == 'r':
                S = 141
            else:
                S = -14
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ESTADO 141
        elif S == 141:
            if i == '>':
                S = 142
            elif i == ' ':
                S = 141
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ESTADO 142
        elif S == 142:
            if i == '#':
                S = 143
            elif i == ' ':
                S = 142
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 143 / EXPRESION REGULAR
        elif S == 143:
            if i.isalnum():
                S = 143
            elif i == '<':
                S = 144
            elif i == ' ':
                S = 143
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 144
        elif S == 144:
            if i == '/':
                S = 145
            else:
                S = -17
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ESTADO 145
        elif S == 145:
            if i == 'c':
                S = 146
            else:
                S = -17
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ESTADO 146
        elif S == 146:
            if i == 'o':
                S = 147
            else:
                S = -17
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ESTADO 147
        elif S == 147:
            if i == 'l':
                S = 148
            else:
                S = -17
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ESTADO 148
        elif S == 148:
            if i == 'o':
                S = 149
            else:
                S = -17
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ESTADO 149
        elif S == 149:
            if i == 'r':
                S = 150
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ESTADO 150
        elif S == 150:
            if i == '>':
                S = 1000
            elif i == ' ':
                S = 150
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "color"', S)
        # ESTADO 1000
        elif S == 1000:
            if i == '<':
                S = 86
            elif i == ' ':
                S = 1000
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 151
        elif S == 151:
            if i == 'e':
                S = 152
            else:
                S = -18
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 152
        elif S == 152:
            if i == 's':
                S = 153
            else:
                S = -18
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 153
        elif S == 153:
            if i == 't':
                S = 154
            else:
                S = -18
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 154
        elif S == 154:
            if i == 'a':
                S = 155
            else:
                S = -18
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 155
        elif S == 155:
            if i == 'c':
                S = 156
            else:
                S = -18
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 156
        elif S == 156:
            if i == 'i':
                S = 157
            else:
                S = -18
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 157
        elif S == 157:
            if i == 'o':
                S = 158
            else:
                S = -18
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 158
        elif S == 158:
            if i == 'n':
                S = 159
            else:
                S = -18
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 159
        elif S == 159:
            if i == '>':
                S = 0
            elif i == ' ':
                S = 159
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "estacion"', S)
        # ESTADO 160
        elif S == 160:
            if i == 'o':
                S = 161
            else:
                S = -19
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 161
        elif S == 161:
            if i == 'm':
                S = 162
            else:
                S = -19
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 162
        elif S == 162:
            if i == 'b':
                S = 163
            else:
                S = -19
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 163
        elif S == 163:
            if i == 'r':
                S = 164
            else:
                S = -19
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 164
        elif S == 164:
            if i == 'e':
                S = 165
            else:
                S = -19
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 165
        elif S == 165:
            if i == '>':
                S = 166
            elif i == ' ':
                S = 165
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 166 / EXPRESION REGULAR
        elif S == 166:
            if i.isalpha():
                S = 167
            elif i == ' ':
                S = 166
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 167 / EXPRESION REGULAR
        elif S == 167:
            if i.isalnum() or i in especiales:
                S = 167
            elif i == '<':
                S = 168
            elif i == ' ':
                S = 167
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Caracter invalido', S)
        # ESTADO 168
        elif S == 168:
            if i == '/':
                S = 169
            else:
                S = -20
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 169
        elif S == 169:
            if i == 'n':
                S = 170
            else:
                S = -20
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 170
        elif S == 170:
            if i == 'o':
                S = 171
            else:
                S = -20
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 171
        elif S == 171:
            if i == 'm':
                S = 172
            else:
                S = -20
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 172
        elif S == 172:
            if i == 'b':
                S = 173
            else:
                S = -20
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 173
        elif S == 173:
            if i == 'r':
                S = 174
            else:
                S = -20
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 174
        elif S == 174:
            if i == 'e':
                S = 175
            else:
                S = -20
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        # ESTADO 175
        elif S == 175:
            if i == '>':
                S = 0
            elif i == ' ':
                S = 175
            else:
                Error = True
                GraficarErrores(fila, columna, i, 'Error en etiqueta "nombre"', S)
        columna = columna + 1
    # print('Estado: ' + str(S))
