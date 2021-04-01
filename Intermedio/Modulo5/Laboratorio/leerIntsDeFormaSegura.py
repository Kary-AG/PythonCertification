#Escenario
#Tu tarea es escribir una función capaz de ingresar valores enteros
#y verificar si están dentro de un rango especificado.
def readint(prompt, min, max):
    try:
        if int(prompt)>min and int(prompt)<max:
            return int(prompt)
        else:
            print("Error: el valor no está dentro del rango permitido (",min,"..",max,")")
            readint(input("Ingresa un numero de -10 a 10: "),min,max)
    except:
        print("Error: entrada incorrecta")
        readint(input("Ingresa un numero de -10 a 10: "),min,max)

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)
