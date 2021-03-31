#Si el número del año no es divisible entre cuatro, es un año común.
#De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
#De lo contrario, si el número del año no es divisible entre 400, es un año común.
#De lo contrario, es un año bisiesto.
year = int(input("Introduzca un año:"))

if(year%4 == 0) and (year%100 !=0):
    print("Año bisiesto")
elif (year % 100 == 0) and (year % 400 == 0) and (year %4 == 0):
    print("Año bisiesto")
else:
    print("Año Común")
# impresión multilínea  utilizar comillas triples para imprimir
# cadenas en varias líneas para facilitar la lectura del texto o
# crear un diseño especial basado en texto.
