#ESCENARIO
#Espatifilo, más comúnmente conocida como la planta de Cuna de Moisés
#o flor de la paz, es una de las plantas para interiores más populares
#que filtra las toxinas dañinas del aire. Algunas de las toxinas que
#neutraliza incluyen benceno, formaldehído y amoníaco.


#Escribe un programa que utilice el concepto de ejecución condicional,
#tome una cadena como entrada y que:
# -Imprima el enunciado "Si, ¡El Espatifilo es la mejor planta de todos
# los tiempos!"  en la pantalla si la cadena ingresada es "Espatifilo".
#  -Imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada
#  es "espatifilo".
#   -Imprima  "¡Espatifilo! ¡No [entrada]!"  de lo contrario.
#   Nota: [entrada] es la cadena que se toma como entrada.

cadena = str(input())

if cadena == "Espatifilo":
    print("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
elif cadena == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo! ¡No",cadena,"!")
