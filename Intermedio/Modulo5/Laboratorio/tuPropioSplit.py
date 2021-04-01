#!/usr/bin/env python3

#ESCENARIO
#Tu tarea es escribir tu propia función, que se comporte casi como el método original split(), por ejemplo:

#Debe aceptar únicamente un argumento: una cadena.
#Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los lugares donde la cadena contiene espacios en blanco.
#Si la cadena está vacía, la función debería devolver una lista vacía.
#Su nombre debe ser misplit().
def misplit(strng):
    l = []
    strng.strip()
    n = strng.find(' ')
    while n!= -1:
        l = l + [strng[:n]]
        strng = strng[n+1:]
        strng.strip()
        n = strng.find(' ')
        if '' in l:
            l.remove('')
    return l

print(misplit2("Ser o no ser, esa es la pregunta"))
print(misplit2("Ser o no ser,esa es la pregunta"))
print(misplit2("   "))
print(misplit2(" abc "))
print(misplit2(""))
