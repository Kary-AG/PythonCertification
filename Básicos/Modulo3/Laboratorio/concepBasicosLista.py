#Escenario
#Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista.
#El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.
miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nuevaLista = []
for numero in miLista:
    if numero not in nuevaLista:
        nuevaLista = nuevaLista + [numero]
        continue
miLista = nuevaLista[:]
print("La lista solo con elementos únicos:")
print(miLista)

a=1
b=0
c=a&b
d=a|b
e=a^b
print(c+d+e)
