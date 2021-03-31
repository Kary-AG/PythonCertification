print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

#Un argumento de palabra clave consta de
#tres elementos: una palabra clave que identifica
#el argumento (end -termina aquí); un signo de igual (=);
#y un valor asignado a ese argumento.
#
#Cualquier argumento de palabra clave debe ponerse después
#del último argumento posicional (esto es muy importante).

#El argumento de palabra clave que puede hacer esto se
#denomina sep (como separador).

print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

#Ambos argumentos de palabras clave pueden mezclarse
#en una invocación, como aquí en la ventana del editor.

print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
