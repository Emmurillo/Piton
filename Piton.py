#------------------------------------------------------------
# Piton.py
# Written by: Esteban & Emmanuel Murillo
# ------------------------------------------------------------

from PitonYacc import yacc, errores_yacc
from PitonLex import lex, errores,lexer

try:
    file = raw_input("Inserte el nombre del archivo")
    fo = open("Examples/" + file +".pi", "r")
    s = fo.read()

    lexer.input(s)

    for tok in iter(lex.token, None):
        # print repr(tok.type), ":", repr(tok.value)
        continue

    largo = len(errores)
    for i in range(largo):
        print "Caracter invalido:", errores[i].value[0], "en la linea:", errores[i].lineno
    lexer.lineno = 1

    yacc.parse(
    input = s,
    lexer = lexer,
    debug = 0)

    print "Analisis finalizado"

except EOFError as e:
    print e.message





