#Escenario
#Tu tarea es escribir un programa que responda la siguiente pregunta:
#¿Los caracteres que comprenden la primera cadena están ocultos dentro de la segunda cadena?

#Por ejemplo:

#Si la segunda cadena es "vcxzxduybfdsobywuefgas", la respuesta es si.
#Si la segunda cadena es "vcxzxdcybfdstbywuefsas", la respuesta es no (ya que no están las letras "d", "o", "g", ni en ese orden).

def findP(strng1, strng2):
    for i in strng1:
        if i not in strng2:
            return "No"
    return "Si"
print(findP("donor", "Nabucodonosor"))
