#------------------------------------------------------------
# Piton.py
# Written by: Esteban & Emmanuel Murillo
# ------------------------------------------------------------

import sys
from PitonYacc import yacc


if sys.version_info[0] >= 3:
    raw_input = input

while True:
    try:
        s = raw_input('Piton > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)

