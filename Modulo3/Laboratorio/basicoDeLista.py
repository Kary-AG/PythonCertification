#ESCENARIO
#Había una vez un sombrero.
#El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4 y 5.
#Tu tarea es
listaSombrero = [1, 2, 3, 4, 5] # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# para reemplazar el número de en medio con un número entero ingresado por el usuario.
listaSombrero[2]=int(input("Ingrese un número para reemplazar"))
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del(listaSombrero[-1])
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print(len(listaSombrero))
print(listaSombrero)
