#The Beatles
#La banda sufrió muchos cambios de formación, que culminaron en 1962 con la formación de John Lennon,
#Paul McCartney, George Harrison y Richard Starkey (mejor conocido como Ringo Starr).
#Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas.
#Tu tarea es:
# paso 1  Crea una lista vacía llamada beatles.
beatles =[]
print("Paso 1:", beatles)

# paso 2  Emplea el método append() para agregar los siguientes miembros de la banda a la lista:
# John Lennon, Paul McCartney y George Harrison
beatles.append("John Lennon", "Paul McCartney","George Harrison")

print("Paso 2:", beatles)

# paso 3 Emplea el ciclofor y el append() para pedirle al usuario que agregue los siguientes
# miembros de la banda a la lista: Stu Sutcliffe, y Pete Best.
print("Paso 3:", beatles)
for i in beatles:
    n =str(input("Ingrese el miembro de la banda:"))
    if n == "Stu Sutcliffe" or n == "Pete Best":
        beatles.append(n)
        break
    continue

# etapa 4  Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
del(beatles[-1])
del(beatles[-2])
print("Paso 4:", beatles)



# paso 5 Usa el método insert() para agregar a Ringo Starr al principio de la lista.
print("Paso 5:", beatles)
beatles.insert(0,"Ringo Starr")

# probando la longitud de la lista
print("Los Fab", len(beatles))
