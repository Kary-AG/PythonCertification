#Escenario
# Tu tarea es escribir un programa que:

#Le pida al usuario algún texto.
#Compruebe si el texto introducido es un palíndromo e imprima el resultado.
def palindromos(strng):
    n = -1
    for i in strng:
        if i == strng[n]:
          n-=1
          continue
        else:

            return "No es un palíndromo"
    return "Es un palíndromo"

s = "Ten animals I slam in a net"
s = s.replace(" ", "").upper()

print(palindromos(s))
