#------------------------------------------------------------
# PitonLex.py
# Regex
#
# Parser
# Written by: Esteban & Emmanuel Murillo
# ------------------------------------------------------------

import ply.lex as lex
import sys

# Palabras reservadas
reserved = {
	'defina' : 'DEFINA',
   	'si' : 'SI',
   	'sino' : 'SINO',
   	'para' : 'PARA',
   	'mientras' : 'MIENTRAS',
   	'retorne' : 'RETORNE',
   	'interruptor' : 'INTERRUPTOR',
   	'caso' : 'CASO',
   	'rango' : 'RANGO',
   	'pare' : 'PARE',	   	
   	'anexar' : 'ANEXAR',
   	'aleatorio' : 'ALEATORIO',
   	'elevar' : 'ELEVAR',
   	'raizc' : 'RAIZC',
   	'mostrar' : 'MOSTRAR',
   	'largo' : 'LARGO',
   	'lanzar' : 'LANZAR',
   	'verdadero' : 'VERDADERO',
   	'falso' : 'FALSO',
   	'and' : 'AND',
   	'or' : 'OR'
}

# Tokens
tokens = ['LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'ASSIGNMENT', 'COMP', 'LESS', 'LESSEQ', 'GREATER', 'GREATEREQ', 'PLUS', 'MINUS', 'STAR', 'SLASH', 'PLUSEQ', 'MINUSEQ', 'STAREQ', 'SLASHEQ', 'COLON', 'COMMA', 'STRING', 'ID', 'INT'] + list(reserved.values())
	
# Expresiones regulares de los tokens
t_LPAREN		=		r'\('
t_RPAREN		=		r'\)'
t_LBRACKET		=		r'\['
t_RBRACKET		=		r'\]'
t_ASSIGNMENT 	= 		r'\='
t_COMP			= 		r'\=='
t_LESS			=		r'\<'
t_LESSEQ		=		r'\<='
t_GREATER		=		r'\>'
t_GREATEREQ		=		r'\>='
t_PLUS			= 		r'\+'
t_MINUS			= 		r'\-'
t_STAR			=		r'\*'
t_SLASH			=		r'\/'
t_PLUSEQ		= 		r'\+='
t_MINUSEQ		= 		r'\-='
t_STAREQ		=		r'\*='
t_SLASHEQ		=		r'\/='
t_COLON			= 		r'\:'
t_COMMA			=		r'\,'
t_STRING 		= 		r'\".*\"'

# Expresion regular para los ID's
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*' 
	return t

def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    return t
    
t_ignore = r' '

def t_error(t):
	raise TypeError("Caracter invalido '%s'" % t.value[0])
	
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
	
lex.lex()

'''for i in range (10):
	name = "ExampleProgram"
	name += str(i) + ".py"
	try:
		fo = open(name, "r")
		
	except IOError as e:
		print "No se encontro el archivo con nombre", name'''
		
fo = open("ExamplePrograms/ExampleProgram0.py", "r")		
lex.input(fo.read())
try:
	for tok in iter(lex.token, None):
		print (tok.type), (tok.value)
except TypeError as e:
	print "Error en la linea", tok.lineno, "posicion", tok.lexpos
	print e
	

