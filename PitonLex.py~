import ply.lex as lex

tokens = ['ID', 'INT']
	
# Expresion regular para los ID's
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*' 
	'''if t.value in reserved:
		t.type = reserved[t.value]'''
	return t

def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    return t
    
t_ignore = r' '

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value))

lex.lex()

lex.input("CH3COOH hola 3 ' f")
try:
	for tok in iter(lex.token, None):
		print repr(tok.type), repr(tok.value)
except TypeError as e:
	print e
