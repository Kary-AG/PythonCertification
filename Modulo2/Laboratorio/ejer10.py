#ESCENARIO
#Millas y kilómetros son unidades de longitud o distancia.

#Teniendo en mente que 1 equivale aproximadamente a 1.61 kilómetros,
#complemente el programa en el editor para que convierta de:

#Millas a kilómetros.
#Kilómetros a millas.

#Notas
#Es la función round(). Su trabajo es redondear la salida del resultado
#al numero de decimales especificados en el paréntesis, y regresar un valor flotante

kilometros = 12.25
millas = 7.38

millas_a_kilometros = millas*1.61/1
kilometros_a_millas = kilometros*1/1.61

print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")
