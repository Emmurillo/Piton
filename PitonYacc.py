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

# Falta declarar todas las reglas gramaticales

def p_program_func(p):
	'program : def_func'
	p[0] = p[1]
	
def p_program_sent(p):
	'program : lista_sentencias'
	p[0] = p[1]
	
def p_def_func(p):
	'def_func : DEFINA nombre LPAREN lista_parametros RPAREN COLON lista_sentencias'
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
	'lista_parametros : '
	pass
	
def p_parametro(p):
	'parametro : ID'
	p[0] = p[1]
	
def p_lista_sentencias_sentencia(p):
	'lista_sentencias : sentencia lista_sentencias'
	p[0] = [p[1]] + p[2]
	
def p_lista_sentencias_vacia(p):
	'lista_sentencias : '
	pass
	
def p_sentencia_asignacion(p):
	'sentencia : asignacion'
	p[0] = p[1]
	
def p_sentencia_condicional(p):
	'sentencia : condicional'
	p[0] = p[1]
	
def p_sentencia_bucle(p):
	'sentencia : bucle'
	p[0] = p[1]
	
'''	
def p_sentencia_reservada(p):
	'sentencia : RESERVED'
	p[0] = p[1]
'''

def p_sentencia_retorne(p):
	'sentencia : RETORNE'
	p[0] = p[1]
	
def p_asignacion_dato(p):
	'asignacion : ID ASSIGNMENT dato'
	names[p[1]] = p[3]
	
'''	
def p_asignacion_lista_operaciones(p):
	'asignacion : lista_operaciones'
	names[p[1]] = p[3]
	
def p_lista_operaciones(p):
	'lista_operaciones : 
'''

def p_dato(p):
	'''dato : INT
			| TRUE
			| FALSE
			| STRING '''


	
def p_error(p):
    if p:
        print("Error de sintaxis @ '%s'" % p.value)
    else:
        print("Error de sintaxis @ EOF")
	
yacc.yacc()
