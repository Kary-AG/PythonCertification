# Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores,
# y generar la altura de la pirámide que se puede construir utilizando estos bloques.

bloques = int(input("Ingrese el número de bloques:"))
altura = 0
num = bloques
while bloques>0:
    altura +=1
    bloques = bloques-altura
if num%altura != 0:
    altura -= 1

print("La altura de la pirámide:", altura)
