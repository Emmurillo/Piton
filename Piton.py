#------------------------------------------------------------
# Piton.py
# Written by: Esteban & Emmanuel Murillo
# ------------------------------------------------------------

from PitonYacc import yacc
from PitonLex import lex, errores

try:
    with open("Examples/grammar.pi", "r") as fo:
        s = fo.read()

    lex.input(s)

    for tok in iter(lex.token, None):
        #print repr(tok.type), ":", repr(tok.value)
        continue

    largo = len(errores)
    print "Cantidad de errres lexicos:", largo
    for i in range (largo):
        print "Caracter invalido:", errores[i].value[0], "en la linea:", errores[i].lineno

except EOFError as e:
    print e

yacc.parse(s)

