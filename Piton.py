#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Librerias y configuracion
import sys

import re
sys.path.insert(0,"../..")

if sys.version_info[0] >= 3:
    raw_input = input

    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#  ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗███████╗
#  ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔════╝
#     ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║███████╗
#     ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║╚════██║
#     ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║███████║
#     ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝
#                                                                                


# Construir lex

#Importar bibliotecas de expresiones regulares


#Lista de tokens 

tokens = [
    'CONDICIONAL_SI','CONDICIONAL_ENTONCES',
    'BUCLE_MIENTRAS','BUCLE_PARA','PARE','BUCLE_SIGA',
    'IMPRIMIR','LEER',
    'VARIABLE','VALOR_ENTERO','VALOR_FLOTANTE','VALOR_CADENA','VALOR_BOOLEANO',
    'PARENTESIS_IZQUIERDO','PARENTESIS_DERECHO',
    'INICIO_SEGMENTO','FIN_SEGMENTO',
    'PARENTESIS_CUADRADO_IZQUIERDO','PARENTESIS_CUADRADO_DERECHO','COMA','OPERACION_ASIGNACION',
    'OPERACION_SUMA','OPERACION_RESTA','OPERACION_MULTIPLICACION','OPERACION_DIVISION','OPERACION_POTENCIA',
    'OPERADOR_LOGICO','COMPARADOR_LOGICO','OPERADOR_ASERCION','EXCEPCIONAL_TRY','EXCEPCIONAL_EXCEPT',
    'OPERADOR_INCLUSION','FUNCION','FIN_ARCHIVO', 'COMENTARIOS','IMPORTACION_BIBLIOTECA',
    'ASIGNACION_PUNTERO','OPERACION_MODULO','RANGO']

errores = "\n____________________________________________"+ \
                 "\n\nLISTA DE ERRORES\n"           # Es un string que imprimir al final cuales fueron los errores léxicos
comp = "\n____________________________________________"+ \
             "\n\nLISTA DE ERRORES\n"   



lineCount=0
lineCountSemantic = 0



#  ██████╗ ███████╗ ██████╗ ███████╗██╗  ██╗
#  ██╔══██╗██╔════╝██╔════╝ ██╔════╝╚██╗██╔╝
#  ██████╔╝█████╗  ██║  ███╗█████╗   ╚███╔╝ 
#  ██╔══██╗██╔══╝  ██║   ██║██╔══╝   ██╔██╗ 
#  ██║  ██║███████╗╚██████╔╝███████╗██╔╝ ██╗
#  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
#                                           

# Definicion de Tokens

t_OPERACION_SUMA     = r'\+'
t_OPERACION_RESTA  = r'-'
t_OPERACION_MULTIPLICACION     = r'\*'
t_OPERACION_DIVISION  = r'/'
t_COMA     = r'\,'
t_OPERACION_ASIGNACION  = r'='
t_COMPARADOR_LOGICO     = r'==|!=|<|>|<=|>='
t_PARENTESIS_IZQUIERDO  = r'\('
t_PARENTESIS_DERECHO  = r'\)'
t_FIN_ARCHIVO    = r'\EOF'
t_INICIO_SEGMENTO = r':'
t_FIN_SEGMENTO = r'\;'
t_PARENTESIS_CUADRADO_IZQUIERDO = r'\['
t_PARENTESIS_CUADRADO_DERECHO = r'\]'
t_OPERACION_MODULO = r'\%'

#Palabras Reservadas
def t_CONDICIONAL_SI(t):
    r'si' # Equivalente al if de python
    return t

def t_CONDICIONAL_ENTONCES(t):
    r'entonces' # Equivalente al else de python
    return t

def t_BUCLE_MIENTRAS(t):
    r'mientras' # Equivalente al while de python
    return t

def t_RANGO(t):
    r'rango' # Equivalente al range de python
    return t

def t_BUCLE_PARA(t):
    r'para' # Equivalente al for de python
    return t

def t_PARE(t):
    r'pare' # Equivalente al break de python
    return t

def t_BUCLE_SIGA(t):
    r'continue' # Equivalente al continue de python
    return t

def t_IMPRIMIR(t):
    r'imprimir'# Equivalente al print de python
    return t

def t_LEER(t):
    r'leer'# Equivalente al input de python
    return t

def t_OPERADOR_LOGICO(t):
    r'&&|//|!!' # Equivalente al and or y not de python
    return t

def t_VALOR_BOOLEANO(t):
    r'cierto|falso' # Equivalente al true/false de python
    return t

def t_OPERADOR_ASERCION(t):
    r'acierto' # Equivalente al assert de python
    return t

def t_EXCEPCIONAL_TRY(t):
    r'intente' # Equivalente al try de python
    return t

def t_EXCEPCIONAL_EXCEPT(t):
    r'excepcion' # Equivalente al except de python
    return t

def t_OPERADOR_INCLUSION(t):
    r'entre' # Equivalente al in(si un elemento esta dentro de la lista) de python
    return t

def t_IMPORTACION_BIBLIOTECA(t):
    r'importar' # Equivalente al import de python
    return t

def t_FUNCION(t):
    r'funcion' # Equivalente al def de python
    return t

def t_ASIGNACION_PUNTERO(t):
    r'asigne' # Equivalente al is(asignacion dinámica) de python
    return t

def t_OPERACION_POTENCIA(t):
    r'eleva' # Equivalente al pow de python
    return t



# Definicion de variable (utiliza el formato estandar de python)
def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    
    t.value = str(t.value)
    
    return t

#Comentarios
def t_COMENTARIOS(t):
    r'\#.*'
    pass #Se desecha el token por que los comentarios no tienen ningun valor

#Definición de un valor entero
def t_VALOR_ENTERO(t):
    r'-?\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Entero no valido: %s" % t.value)
        t.value = 0
    return t

#Definición de un valor flotante(Expresiones regulares utilizadas de la biblioteca re)
def t_VALOR_FLOTANTE(t):
    r'[-+]?(?:\b[0-9]+(?:\.[0-9]*)?|\.[0-9]+\b)(?:[eE][-+]?[0-9]+\b)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Flotante no valido: %s" % t.value)
        t.value = 0
    return t

#Definición de un valor string
def t_VALOR_CADENA(t):
    r'\"([^\\"]|(\\.))*\"'
    escape = 0 # Verfica los caracteres de escape
    str = t.value[1:-1]
    nueva_cadena = ""
    for i in range(0, len(str)):
        c = str[i]
        if escape:
            if c == "n":
                c = "\n"
            elif c == "t":
                c = "\t"
            nueva_cadena += c
            escape = 0
        else:
            if c == "\\":
                escape = 1
            else:
                nueva_cadena += c
    t.value = nueva_cadena
    return t



t_ignore = " "

#Definición de cambio de linea
def t_DELIMITADOR(t):
    r'\n+'
    global lineCount
    global lineCountSemantic
    lineCount += t.value.count("\n")
    if t.value.count("\n")-1 == 0:
        lineCountSemantic+= 1
    else:
        lineCountSemantic+= t.value.count("\n")

#Verifica si el token no genera las expresiones regulares definidas    
def t_error(t):
    global errores
    global lineCount
    errores += "CARACTER INVALIDO: No identificado '%s' en la linea %d \n" % (t.value[0], lineCount)
    t.lexer.skip(1)
    
    
import ply.lex as lex
lexer = lex.lex(optimize = 1)




#   ██████╗ ██████╗  █████╗ ███╗   ███╗███╗   ███╗ █████╗ ██████╗ 
#  ██╔════╝ ██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔══██╗██╔══██╗
#  ██║  ███╗██████╔╝███████║██╔████╔██║██╔████╔██║███████║██████╔╝
#  ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══██╗
#  ╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║  ██║
#   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
#                                                                 


# Parsing de las reglas de la gramatica

precedence = (
    ('left','OPERACION_POTENCIA'),
    ('left','OPERACION_SUMA','OPERACION_RESTA'),
    ('left','OPERACION_MULTIPLICACION','OPERACION_DIVISION','OPERACION_MODULO'),
    ('right','UMINUS'),
    )

# diccionario de identificadores
names = { }

# Reglas de la gramatica

def p_regla_programa(t):
    'programa : lista_sentencias'
    t[0] = t[1]


def p_regla_sentencias(t):
    'lista_sentencias : sentencia lista_sentencias'
    t[0] = t[1]

def p_regla_sentencia_2(t):
    'lista_sentencias : sentencia'
    t[0] = t[1]

def p_regla_sentencia_end(t):
    'lista_sentencias : FIN_ARCHIVO'
    t[0] = t[1]

def p_regla_funciones(t):
    'sentencia : FUNCION VARIABLE PARENTESIS_IZQUIERDO lista_variables PARENTESIS_DERECHO INICIO_SEGMENTO lista_sentencias FIN_SEGMENTO'
    t[0] = t[4]

def p_regla_funciones2(t):
    'sentencia : FUNCION VARIABLE PARENTESIS_IZQUIERDO PARENTESIS_DERECHO INICIO_SEGMENTO lista_sentencias FIN_SEGMENTO'
    t[0] = t[2]

def p_regla_funciones3(t): 
    'sentencia : FUNCION VARIABLE PARENTESIS_IZQUIERDO PARENTESIS_DERECHO INICIO_SEGMENTO FIN_SEGMENTO'
    t[0] = t[2]

def p_regla_asignar(t):
    'sentencia : VARIABLE OPERACION_ASIGNACION expresion'
    val = str(t[3])
    if val == "cierto":
        names[t[1]] = "cierto"
    elif val == "falso":
        names[t[1]] = "falso"
    else:
        names[t[1]] = t[3]


def p_regla_asignar2(t):
    'sentencia : VARIABLE OPERACION_ASIGNACION VARIABLE'
    names[t[1]] = names[t[3]]

def p_regla_asignar_puntero(t):
    'sentencia : VARIABLE ASIGNACION_PUNTERO expresion'
    names[t[1]] = t[3]

def p_regla_sentencias_lectura(t):
    'sentencia : LEER PARENTESIS_IZQUIERDO lista_variables PARENTESIS_DERECHO'
    entrada=input()
    names[t[3]] = entrada

def p_regla_sentencias_lectura2(t):
    'sentencia : LEER PARENTESIS_IZQUIERDO VARIABLE PARENTESIS_DERECHO'
    global errores
    entrada=input()
    try:
        val = int(entrada)
        names[t[3]] = int(entrada)
    except ValueError:
        try:
            val = float(entrada)
            names[t[3]] = float(entrada)
        except ValueError:
            try:
                val = str(entrada)
                if val == "cierto":
                    names[t[3]] = "cierto"
                elif val == "falso":
                    names[t[3]] = "falso"
                else:
                    names[t[3]] = str(entrada)
            except:
                errores+= "\nSEMANTICO: Tipo de dato desconocido. Linea: "+ str(lineCountSemantic)
    

def p_regla_sentencias_escritura(t):
    'sentencia : IMPRIMIR PARENTESIS_IZQUIERDO lista_expresion PARENTESIS_DERECHO'
    global errores
    try:
        print(t[3])
    except:
        errores+="\nSEMANTICO: Variable indefinida. Linea: "+str(lineCountSemantic)

def p_regla_sentencias_escritura2(t):
    'sentencia : IMPRIMIR PARENTESIS_IZQUIERDO VARIABLE PARENTESIS_DERECHO'
    global errores
    try:
        print(names[t[3]])
    except:
        errores+="\nSEMANTICO: Variable indefinida. Linea: "+str(lineCountSemantic)


def p_regla_excepcionales(t):
    'sentencia : EXCEPCIONAL_TRY lista_sentencias EXCEPCIONAL_EXCEPT lista_sentencias'
    t[0] = t[2]

def p_regla_condicional_si(t):
    'sentencia : CONDICIONAL_SI PARENTESIS_IZQUIERDO condicional PARENTESIS_DERECHO INICIO_SEGMENTO lista_sentencias FIN_SEGMENTO'
    t[0] = t[3]

def p_regla_condicional_entonces(t):
    'sentencia : CONDICIONAL_ENTONCES INICIO_SEGMENTO lista_sentencias FIN_SEGMENTO'
    t[0] = t[3]

def p_regla_comparador(t):
    'expresion : expresion OPERADOR_LOGICO expresion'
    global errores
    if(t[1]=="cierto"):
        t[1]=True
    else:
        t[1]=False
    if(t[3]=="cierto"):
        t[3]=True
    else:
        t[3]=False
    if(((isinstance(t[1],bool) and (isinstance(t[3],bool))))):
        if t[2] == '&&':
            t[0] = t[1] and t[3]
            if t[0]:
                t[0] = "cierto"
            else:
                t[0] = "falso"
            
        elif t[2] == '//':
            t[0] = t[1] or t[3]
            if t[0]:
                t[0] = "cierto"
            else:
                t[0] = "falso"
        
        
    else:
        errores+="\nSEMANTICO: Las expresiones '",type(t[1]), "' y '",type(t[3])," no son comparables. Linea: " +str(lineCountSemantic)

def p_regla_comparador_no(t):
    'expresion : OPERADOR_LOGICO expresion'
    global errores
    if t[2] == "cierto" and t[1] == '!!':
        t[0] = "falso"
    elif t[2] == "falso" and t[1] == '!!':
        t[0] = "cierto"
    else:
       errores += "\nSINTACTICO: Operador necesario en la expresion. Linea: " + str(lineCountSemantic)
       t[0] = t[2]
    
    
def p_regla_comparador2(t):
    'condicional : expresion COMPARADOR_LOGICO expresion'
    t[0] = t[1]

def p_regla_asercion(t):
    'condicional : OPERADOR_ASERCION condicional'
    t[0] = t[1]
    
def p_regla_inclusion(t):
    'condicional : expresion OPERADOR_INCLUSION expresion'
    t[0] = t[1]

def p_regla_lista_variables_termino(t):
    'lista_variables : VARIABLE'
    
def p_regla_lista_variables_inicio(t):
    'lista_variables : lista_variables COMA VARIABLE'

def p_regla_lista_expresion(t):
    'lista_expresion : expresion COMA expresion'
    t[0] = t[1]
     
def p_regla_lista_expresion_termino(t):
    'lista_expresion : expresion'
    t[0] = t[1]

def p_regla_expresion(t):
    'sentencia : expresion'

def p_regla_operacion(t):
    '''expresion : expresion OPERACION_SUMA expresion
                  | expresion OPERACION_RESTA expresion
                  | expresion OPERACION_MULTIPLICACION expresion
                  | expresion OPERACION_DIVISION expresion
                  | expresion OPERACION_MODULO expresion
                  | expresion OPERACION_POTENCIA expresion'''
    global errores

    if t[2] == '+'  :
        if(((isinstance(t[1],(int , float, bool)) and (isinstance(t[3],(int,float, bool))))) or (((isinstance(t[1],str)) and (isinstance(t[3],str))))):
            t[0] = t[1] + t[3]
        else:
            errores+= "\nSEMANTICO: Las expresiones' "+str(type(t[1]))+ " y "+str(type(t[3]))+ " deben ser de tipo entero. Linea: "+ str(lineCountSemantic)
            

    elif t[2] == '-': 
        if(((isinstance(t[1],(int , float, bool)) and (isinstance(t[3],(int,float, bool)))))):
            t[0] = t[1] - t[3]
        else:
            errores+= "\nSEMANTICO: Las expresiones' "+str(type(t[1]))+ " y "+str(type(t[3]))+ " deben ser de tipo entero. Linea: "+ str(lineCountSemantic)
    elif t[2] == '*':
        if(((isinstance(t[1],(int , float, bool)) and (isinstance(t[3],(int,float, bool))))) or (((isinstance(t[1],str)) and (isinstance(t[3],int)))) or (((isinstance(t[1],int)) and (isinstance(t[3],str))))):
            t[0] = t[1] *  t[3]
        else:
            errores+= "\nSEMANTICO: Las expresiones' "+str(type(t[1]))+ " y "+str(type(t[3]))+ " deben ser de tipo entero. Linea: "+ str(lineCountSemantic)
    elif t[2] == '/':
        if(((isinstance(t[1],(int, float)) and (isinstance(t[3],(int,float)))))):
           if(t[3] == 0):
               errores+="\nSEMANTICO: Expresion con division por cero. Linea: "+ str(lineCountSemantic)
           else:
                t[0] = t[1] / t[3]
        else:
            errores+= "\nSEMANTICO: Las expresiones' "+str(type(t[1]))+ " y "+str(type(t[3]))+ " deben ser de tipo entero. Linea: "+ str(lineCountSemantic)
            
    elif t[2] == '%':
        if(((isinstance(t[1],(int, float)) and (isinstance(t[3],(int,float)))))):
           if(t[3] == 0):
               errores+="\nSEMANTICO: Cero no permite modulo"
           else:
                t[0] = t[1] % t[3]
        else:
            errores+= "\nSEMANTICO: Las expresiones' "+str(type(t[1]))+ " y "+str(type(t[3]))+ " deben ser de tipo entero. Linea: "+ str(lineCountSemantic)
    elif t[2] == 'eleva':
        if(((isinstance(t[1],(int, float)) and (isinstance(t[3],(int,float)))))):
           if(t[3] == 0 and t[1] == 0):
               errores+="\nSEMANTICO: Cero no es elevable en base cero"
           else:
                t[0] = pow(t[1],t[3])
        else:
            errores+= "\nSEMANTICO: Las expresiones' "+str(type(t[1]))+ " y "+str(type(t[3]))+ " deben ser de tipo entero. Linea: "+ str(lineCountSemantic)


def p_expresion_uminus(t):
    'expresion : OPERACION_RESTA expresion %prec UMINUS'
    t[0] = -t[2]

def p_regla_grupo(t):
    'expresion : PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO'
    t[0] = t[2]

def p_regla_numero(t):
    'expresion : VALOR_ENTERO'
    t[0] = t[1]

def p_regla_flotante(t):
    'expresion : VALOR_FLOTANTE'
    t[0] = t[1]

def p_regla_booleano(t):
    'expresion : VALOR_BOOLEANO'
    t[0]=t[1]
    
def p_regla_cadena(t):
    'expresion : VALOR_CADENA'
    t[0] = t[1]

def p_regla_lista(t):
    'expresion : VARIABLE OPERACION_ASIGNACION PARENTESIS_CUADRADO_IZQUIERDO lista_constantes PARENTESIS_CUADRADO_DERECHO'
    t[0] = t[2]

def p_regla_constantes_enteras(t):
    'lista_constantes : VALOR_ENTERO COMA lista_constantes'
    t[0] = t[1]

def p_regla_constantes_enteras_end(t):
    'lista_constantes : VALOR_ENTERO'
    t[0] = t[1]

def p_regla_constantes_flotantes(t):
    'lista_constantes : VALOR_FLOTANTE COMA lista_constantes'
    t[0] = t[1]

def p_regla_constantes_floantes_end(t):
    'lista_constantes : VALOR_FLOTANTE'
    t[0] = t[1]

def p_regla_constantes_cadenas(t):
    'lista_constantes : VALOR_CADENA COMA lista_constantes'
    t[0] = t[1]

def p_regla_constantes_cadenas_end(t):
    'lista_constantes : VALOR_CADENA'
    t[0] = t[1]


def p_regla_constantes_booleanas(t):
    'lista_constantes : VALOR_BOOLEANO COMA lista_constantes'
    t[0] = t[1]

def p_regla_constantes_booleanas_end(t):
    'lista_constantes : VALOR_BOOLEANO'
    t[0] = t[1]
    

def p_regla_identificador(t):
    'expresion : VARIABLE'
    global errores
    if(t[1] in names):
        t[0]=names[t[1]]
    else:
        errores+="\nSEMANTICO: Variable "+ str(t[1]) + " indefinida. Linea: " + str(lineCountSemantic)


def p_regla_importacion(t):
    'sentencia : IMPORTACION_BIBLIOTECA VARIABLE'
    t[0] = t[2]

# Reglas para instrucciones iterativas

def p_regla_bucle_terminar(t):
    'sentencia : PARE'
    t[0] = t[1]

def p_regla_bucle_seguir(t):
    'sentencia : BUCLE_SIGA'
    t[0] = t[1]

def p_regla_bucle_para(t):
    'sentencia : BUCLE_PARA VARIABLE OPERADOR_INCLUSION RANGO PARENTESIS_IZQUIERDO sentencia COMA sentencia PARENTESIS_DERECHO INICIO_SEGMENTO lista_sentencias FIN_SEGMENTO'
    t[0] = t[3]

def p_regla_bucle_para2(t):
    'sentencia : BUCLE_PARA VARIABLE OPERADOR_INCLUSION PARENTESIS_IZQUIERDO VARIABLE PARENTESIS_DERECHO INICIO_SEGMENTO lista_sentencias FIN_SEGMENTO'
    t[0] = t[3]

def p_regla_bucle_mientras(t):
    'sentencia : BUCLE_MIENTRAS PARENTESIS_IZQUIERDO condicional PARENTESIS_DERECHO INICIO_SEGMENTO lista_sentencias FIN_SEGMENTO'
    t[0] = t[3]


#######################################################################################################################


def p_regla_comentarios(t):
    'sentencia : sentencia COMENTARIOS'
    t[0] = t[1]

    
def p_error(t):
    global errores
    global lineCount
    if t:
        errores+= "\nSINTACTICO: Token '%s' inesperado en la linea %d" % (t.value, lineCount) + "\n"
    else:
        errores+= "\nSINTACTICO: En EOF"  + "\n"

            

# Construir yacc
import ply.yacc as yacc
yacc.yacc(optimize = 1)
        
def verificarErrores(errores):
    if(len(errores)>len(comp)): #Aqui hubo errores léxicos
        print bcolors.WARNING, errores, bcolors.ENDC
        print bcolors.FAIL,"\nTraducción finalizada con errores\n", bcolors.ENDC
    else: # Todos los tokens son validos
        #print errores
        print bcolors.OKGREEN,"\nTraducción finalizada sin errores\n", bcolors.ENDC

#  ███╗   ███╗ █████╗ ██╗███╗   ██╗
#  ████╗ ████║██╔══██╗██║████╗  ██║
#  ██╔████╔██║███████║██║██╔██╗ ██║
#  ██║╚██╔╝██║██╔══██║██║██║╚██╗██║
#  ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
#  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
#                                  


# Archivo para analizar
file = "Examples/micodigo"

with open (file+".pi", "r") as myfile:
    data=myfile.read()

# Configurar entrada de lex
lexer.input(data)


# Imprimir los tokens encontrados
print("LISTA DE TOKENS")
while True:
    tok = lexer.token()
    if not tok: 
        break

    print tok.value, '\t\t', tok.type
    
# Imprimir la tabla de simbolos
print("TABLA DE SIMBOLOS")
for name in names:
    print name, '\t\t'

# Reestablecer el contador


lineCount=1
lineCountSemantic = 0
print("\n\n")
yacc.parse(data)
print("\n\n")

verificarErrores(errores) 


