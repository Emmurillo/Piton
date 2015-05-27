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
literals = "\n"

# Para almacenar los nombres de variables
# Sirve para ver si una variable ya fue definida
names = {}

# Lista de errores

errores_yacc = []

# Inicio de la definicion de la gramatica  

# Definicion de funciones
def p_program_def(p):
	"""program 	: definicion
            	| sentencias"""

# Definicion basica de las funciones
def p_definicion_func(p):
	'definicion : DEFINA ID LPAREN params RPAREN COLON sentencias SEMICOLON'

# Parametros
def p_params(p):
	"""params 	: lista_params
                | empty"""

def p_lista_params(p):
	"""lista_params : ID
                	| lista_params COMMA ID"""

# Definicion de las sentencias
def p_sentencias(p):
	"""sentencias	: sentencia
                	| lista_sentencias"""

def p_lista_sentencias(p):
	"""lista_sentencias : sentencia lista_sentencias
                		| empty"""

 # CAMBIAR POR NEWLINE
def p_sentencia(p):
	"""sentencia 	: asignacion SEMICOLON
                	| condicional SEMICOLON
                	| bucle SEMICOLON
                	| PARE SEMICOLON
                	| operacion SEMICOLON
                	| RETORNE booleano SEMICOLON
                	| RETORNE dato SEMICOLON"""

#Quedan pendientes arreglos para el bucle para
def p_bucle(p):
	"""bucle 	: MIENTRAS expresion COLON sentencias
				| PARA dato EN ID COLON sentencias"""

def p_expresion(p):
	"""expresion 	: booleano
					| dato comp dato
					| operacion comp dato
					| dato comp operacion
					| operacion comp operacion"""

def p_operacion(p):
	"""operacion	: operacion operador operacion
					| LPAREN operacion operador operacion RPAREN
				 	| dato operador dato
				 	| LPAREN dato operador dato RPAREN
				 	| dato operador operacion
				 	| LPAREN dato operador operacion RPAREN
				 	| operacion operador dato
				 	| LPAREN operacion operador dato RPAREN"""

def p_booleano(p):
	"""booleano	: VERDADERO
				| FALSO"""
def p_comp(p):
	"""comp	: COMP
			| LESS
			| LESSEQ
			| GREATER
			| GREATEREQ"""

def p_comp_boolean(p):
	"""compBoolean 	: Y
					| O"""

def p_operador(p):
	"""operador : PLUS
				| MINUS
				| STAR
				| SLASH"""

def p_asignacion_dato(p):
	"""asignacion 	: ID ASSIGNMENT dato
					| ID ASSIGNMENT STRING
					| ID PLUSEQ dato
					| ID MINUSEQ dato
					| ID STAREQ dato
					| ID SLASHEQ dato
					| ID ASSIGNMENT operacion
					| ID PLUSEQ operacion
					| ID MINUSEQ operacion
					| ID STAREQ operacion
					| ID SLASHEQ operacion"""

def p_condicional_si(p):
	"""condicional 	: SI dato COLON sentencias
					| SI dato comp dato COLON sentencias
					| SI dato comp operacion COLON sentencias
					| SI operacion comp dato COLON sentencias
					| SI operacion comp operacion COLON sentencias
					| SI booleano compBoolean booleano COLON sentencias
					| SI dato COLON sentencias SINO COLON sentencias
					| SI dato comp dato COLON sentencias SINO COLON sentencias
					| SI dato comp operacion COLON sentencias SINO COLON sentencias
					| SI operacion comp dato COLON sentencias SINO COLON sentencias
					| SI operacion comp operacion COLON sentencias SINO COLON sentencias
					| SI booleano compBoolean booleano SINO COLON sentencias"""

# Tipos de datos
def p_dato(p):
	"""dato : INT
			| ID"""

def p_empty(p):
	"""empty : """
	pass

def p_error(p):
    if p:
        print("Error de sintaxis '%s'" % p.value)
    else:
        print("Error de sintaxis")

	
yacc.yacc()


