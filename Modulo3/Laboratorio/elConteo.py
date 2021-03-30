#Tu tarea es muy simple aquí: escribe un programa que use un ciclo for
#para "contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco,
#el programa debería imprimir en la pantalla el mensaje final
#"¡Listo o no, ahí voy!"

#Utiliza el esqueleto que hemos proporcionado en el editor.

import time
# Escribe un ciclo for que cuente hasta cinco.
for i in range(1,6):
# Cuerpo del ciclo: imprime el número de iteración del ciclo y la palabra "Mississippi".
    print(i, "Mississippi")
# Cuerpo del ciclo - uso: time.sleep (1)
    time.sleep(1)
# Escribe una función de impresión con el mensaje final.
print("¡Listo o no, ahí voy!")
