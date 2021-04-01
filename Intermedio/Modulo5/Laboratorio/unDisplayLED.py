#!/usr/bin/env python3
#Escenario
#Tu tarea es escribir un programa que puede simular el funcionamiento de
#un display de siete segmentos, aunque vas a usar LEDs individuales en lugar de segmentos.
#Falta arreglar el print
lstDisplay=['''###
# #
# #
# #
###''','''#
#
#
#
#''','''###
  #
###
#
###''','''###
  #
###
  #
###''','''# #
# #
###
  #
  #''','''###
#
###
  #
###''','''###
#
###
# #
###''','''###
  #
  #
  #
  #''','''###
# #
###
# #
###''','''###
# #
###
  #
###'''
]

def display(num):
    s = str(num)
    n = 0
    ls =[]
    while n < len(s):
        ls = ls +[lstDisplay[int(s[n])]]
        n+=1
    print(ls)
display(123)
