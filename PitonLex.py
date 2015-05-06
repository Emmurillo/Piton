#------------------------------------------------------------
# PitonLex.py
# Regex
#
# Tokenizer
# Written by: Esteban & Emmanuel Murillo
# ------------------------------------------------------------

import sys
import ply.lex as lex
sys.path.insert(0,"../..")

if sys.version_info[0] >= 3:
    raw_input = input
    
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
tokens = ['LPAREN', 'RPAREN', 'ASSIGNMENT', 'COMP', 'LESS', 'LESSEQ', 'GREATER', 'GREATEREQ', 'ADDOP', 'COLON', 'COMMA', 'ID', 'INTLITERAL'] + list(reserved.values())

# Expresiones regulares de los tokens
t_LPAREN		=		r'\('
t_RPAREN		=		r'\)' 
t_ASSIGNMENT 	= 		r'\='
t_COMP			= 		r'\=='
t_LESS			=		r'\<'
t_LESSEQ		=		r'\<='
t_GREATER		=		r'\>'
t_GREATEREQ		=		r'\>='
t_ADDOP			= 		r'[+-]'
t_COLON			= 		r'\:'
t_COMMA			=		r'\,'

# Expresiones regulares de las palabras reservadas
t_DEFINA		=		r'[defina]'
t_SI			=		r'[si]'
t_SINO			=		r'[sino]'
t_PARA			= 		r'[para]'
t_MIENTRAS		=		r'[mientras]'
t_RETORNE		=		r'[retorne]'
t_INTERRUPTOR	=		r'[interruptor]'
t_CASO			=		r'[caso]'
t_RANGO			=		r'[rango]'
t_PARE			=		r'[pare]'
t_ANEXAR		=		r'[anexar]'
t_ALEATORIO		=		r'[aleatorio]'
t_ELEVAR		=		r'[elevar]'
t_RAIZC			=		r'[raizc]'
t_MOSTRAR		=		r'[mostrar]'
t_LARGO			=		r'[largo]'
t_LANZAR		=		r'[lanzar]'
t_VERDADERO		=		r'[Verdadero]'
t_FALSO			=		r'[Falso]'
t_AND			=		r'[and]'
t_OR			=		r'[or]'

# Expresion regular para los ID's
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*' 
	if t.value in reserved:
		t.type = reserved[t.value]
	return t

def t_INTLITERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Caracteres ignorados
#t_ignore = " \t"

# Para ignorar los comentarios
def t_COMMENT(t):
    r'\#.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Para manejar el EOF
def t_eof(t):
    more = raw_input('... ')
    if more:
        t.lexer.input(more)
        return t.lexer.token()
    return None
    
# Build the lexer
lex.lex()



