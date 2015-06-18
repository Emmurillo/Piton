# ------------------------------------------------------------
# PitonLex.py
# Regex
#
# Scanner
# Written by: Esteban & Emmanuel Murillo
# ------------------------------------------------------------

import ply.lex as lex

errores = []

# Palabras reservadas
reserved = {
    'defina': 'DEFINA',
    'si': 'SI',
    'sino': 'SINO',
    'para': 'PARA',
    'mientras': 'MIENTRAS',
    'retorne': 'RETORNE',
    'interruptor': 'INTERRUPTOR',
    'caso': 'CASO',
    'rango': 'RANGO',
    'pare': 'PARE',
    'anexar': 'ANEXAR',
    'aleatorio': 'ALEATORIO',
    'elevar': 'ELEVAR',
    'raizc': 'RAIZC',
    'largo': 'LARGO',
    'lanzar': 'LANZAR',
    'verdadero': 'VERDADERO',
    'falso': 'FALSO',
    'y': 'Y',
    'o': 'O',
    'en': 'EN',
    'imprimir': 'IMPRIMIR'
}

# Tokens
tokens = ['LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE',
          'ASSIGNMENT', 'COMP', 'LESS', 'LESSEQ', 'GREATER', 'GREATEREQ', 'PLUS',
          'MINUS', 'STAR', 'SLASH', 'PLUSEQ', 'MINUSEQ', 'STAREQ', 'SLASHEQ',
          'COLON', 'SEMICOLON', 'COMMA', 'STRING', 'RESERVED', 'ERROR', 'ID',
          'INT', 'NEWLINE'] + list(reserved.values())

# Expresiones regulares de los tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGNMENT = r'\='
t_COMP = r'\=='
t_LESS = r'\<'
t_LESSEQ = r'\<='
t_GREATER = r'\>'
t_GREATEREQ = r'\>='
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_PLUSEQ = r'\+='
t_MINUSEQ = r'\-='
t_STAREQ = r'\*='
t_SLASHEQ = r'\/='
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_STRING = r'\".*\"'
t_NEWLINE = r'\\n'

# Revisar cada una de las palabras reservadas
def t_RESERVED(t):
    r'[a-zA-Z][\w]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Expresion regular para los ID's
def t_ID(t):
    r'[a-zA-Z_$][a-zA-Z_0-9]*'
    t[0] = t[1]
    return t

# Expresion regular para los enteros
def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    print "Num detected ", t.value
    return t

# Expresiones regulares de las palabras reservadas
t_DEFINA = r'[defina]'
t_SI = r'[si]'
t_SINO = r'[sino]'
t_PARA = r'[para]'
t_MIENTRAS = r'[mientras]'
t_RETORNE = r'[retorne]'
t_INTERRUPTOR = r'[interruptor]'
t_CASO = r'[caso]'
t_RANGO = r'[rango]'
t_PARE = r'[pare]'
t_ANEXAR = r'[anexar]'
t_ALEATORIO = r'[aleatorio]'
t_ELEVAR = r'[elevar]'
t_RAIZC = r'[raizc]'
t_IMPRIMIR = r'[imprimir]'
t_LARGO = r'[largo]'
t_LANZAR = r'[lanzar]'
t_VERDADERO = r'[Verdadero]'
t_FALSO = r'[Falso]'
t_Y = r'[y]'
t_O = r'[o]'

# Para ignorar los espacios en blanco
t_ignore = ' \t'

def t_error(t):
    t.lexer.skip(1)
    print
    errores.append(t)

# Para llevar control del numero de linea que se lee, asi se indica en caso de error
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Para ignorar los comentarios
def t_COMMENT(t):
    r'\#.*'
    pass

# Se lee uno de los programas	
lexer = lex.lex()
