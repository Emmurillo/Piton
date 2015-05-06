#------------------------------------------------------------
# PitonYacc.py
# Grammar rules for Piton- programming language
#
# Parser
# Written by: Esteban & Emmanuel Murillo
# ------------------------------------------------------------

import ply.yacc as yacc
from PitonLex import tokens

# Parsing rules
precedence = (('left','ADDOP'), ('right','UMINUS'))

# Para almacenar los nombres de variables
# Sirve para ver si una variable ya fue definida
names = {}

# Falta declarar todas las reglas gramaticales


yacc.yacc()
