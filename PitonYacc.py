#------------------------------------------------------------
# PitonYacc.py
# Grammar rules for Piton programming language
#
# Parser
# Written by: Esteban & Emmanuel Murillo
# ------------------------------------------------------------

import ply.yacc as yacc
from PitonLex import tokens

# Parsing rules
#precedence = (('left','ADDOP'), ('right','UMINUS'))

# Para almacenar los nombres de variables
# Sirve para ver si una variable ya fue definida
names = {}

# Lista de errores

errores_yacc = []

# Inicio de la definicion de la gramatica  

# Definicion de funciones
def p_program_def(p):
	"""program : definicion
                 | sentencias"""


# Definicion basica de las funciones

def p_definicion_func(p):
	'definicion : DEFINA ID LPAREN params RPAREN COLON sentencias SEMICOLON'

# Parametros
def p_params(p):
	"""params : lista_params
                | empty"""

def p_lista_params(p):
	"""lista_params : ID
                | lista_params COMMA ID"""


# Definicion de las sentencias


def p_sentencias(p):          # CAMBIAR POR NEWLINE
	"""sentencias : sentencia SEMICOLON
                | lista_sentencias"""

def p_lista_sentencias(p):          # CAMBIAR POR NEWLINE
	"""lista_sentencias : sentencia SEMICOLON lista_sentencias
                | empty"""

def p_sentencia(p):          # CAMBIAR POR NEWLINE
	"""sentencia : asignacion
                    | condicional"""

def p_asignacion_dato(p):
	'asignacion : ID ASSIGNMENT dato'

# Condicional

def p_condicional_si(p):
    'condicional : SI dato COLON sentencias'


# Tipos de datos
def p_dato(p):
	"""dato : INT
			| VERDADERO
			| ID
			| FALSO
			| STRING"""


# Hilera vacia

def p_empty(p):
	'empty :'
	pass


'''
	
def p_program_sent(p):
	'program : lista_sentencias'
	p[0] = p[1]
	
def p_def_func(p):
	'def_func : DEFINA nombre LPAREN lista_parametros RPAREN COLON lista_sentencias SEMICOLON'
	p[0] = p[1]
	
def p_nombre(p):
	'nombre : ID'
	p[0] = p[1]
	
def p_lista_parametros_parametro(p):
	'lista_parametros : parametro lista_parametros'
	p[0] = [p[1]] + p[2]
	
def p_lista_parametros_comma(p):
	'lista_parametros : COMMA parametro lista_parametros'
	p[0] = [p[2]] + p[3]
	
def p_lista_parametros_vacia(p):
	'lista_parametros : empty'
	p[0] = []
	

	
def p_parametro(p):
	'parametro : ID'
	p[0] = p[1]
	
def p_lista_sentencias_sentencia(p):
	'lista_sentencias : sentencia lista_sentencias'
	p[0] = [p[1]] + p[2]
	
def p_lista_sentencias_vacia(p):
	'lista_sentencias : empty'
	p[0] = []
	
def p_sentencia_asignacion(p):
	'sentencia : asignacion NEWLINE'
	p[0] = p[1]
	

def p_sentencia_condicional(p):
	'sentencia : condicional NEWLINE'
	p[0] = p[1]
	
def p_sentencia_bucle(p):
	'sentencia : bucle NEWLINE'
	p[0] = p[1]
	sdf% := 'das'
	

def p_sentencia_reservada(p):
	'sentencia : RESERVED'
	p[0] = p[1]


def p_sentencia_retorne(p):
	'sentencia : RETORNE'
	p[0] = p[1]
	

def p_asignacion_lista_operaciones(p):
	'asignacion : lista_operaciones'
	names[p[1]] = p[3]
	

'''
	
def p_error(p):
    if p:
        print("Error de sintaxis '%s'" % p.value)
    else:
        print("Error de sintaxis" )

	
yacc.yacc()


