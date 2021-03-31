# scribe un programa que lea un número natural y ejecute los pasos anteriores
# siempre que c0 sea diferente de 1. También queremos que cuente los pasos necesarios
# para lograr el objetivo. Tu código también debe mostrar todos los valores intermedios de c0.
#Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0.
#Si es par, evalúa un nuevo c0 como c0 ÷ 2.
#De lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1.
#Si c0 ≠ 1, salta al punto 2.

c0 = int(input())
if c0<=0:
    print("El número no es valido")
contador = 0
while c0!=1:
    contador +=1
    if c0%2 == 0:
        c0 = c0//2
        print(c0)
    else:
        c0 = 3*c0+1
        print(c0)
print("pasos =", contador)
