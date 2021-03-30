#Escribe un programa que use:

palabraSinVocal = ""

# Indicar al usuario que ingrese una palabra
palabra = input()
# y asignarlo a la variable userWord
palabra= palabra.upper()

for i in palabra:
    if (i != "A") and (i != "E") and (i!="I") and (i !="O") and (i !="U"):
        palabraSinVocal = palabraSinVocal + i
print(palabraSinVocal)
# Completa el cuerpo del ciclo.
# Imprimir la palabra asignada a palabraSinVocal.
