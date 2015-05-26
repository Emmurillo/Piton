#------------------------------------------------------------
# Piton.py
# Written by: Esteban & Emmanuel Murillo
# ------------------------------------------------------------

from PitonYacc import yacc

try:
    fo = open("Examples/grammar.pi", "r")
    s = fo.read()
except EOFError as e:
    print e

yacc.parse(s)

# Para leer tokens y detectar errores lexicos
"""
fo = open("Examples/.pi", "r")

lex.input(fo.read())

for tok in iter(lex.token, None):
    print repr(tok.type), ":", repr(tok.value)

largo = len(errores)
print "Cantidad de errres lexicos:", largo
for i in range (largo):
    print "Caracter invalido:", errores[i].value[0], "en la linea:", errores[i].lineno
"""



