#Escenario
#Tu tarea es escribir un programa que:

#Le pida al usuario dos textos por separado.
#Compruebe si los textos ingresados son anagramas e imprima el resultado.
def anagramas(strng1,strng2 ):
    strng1 = strng1.replace(" ","").upper()
    strng2 = strng2.replace(" ","").upper()
    if len(strng1) != len(strng2):
        return "No son Anagramas"
    else:
        for i in strng1:
            if i in strng2:
                continue
            else:
                return "No son Anagramas"
        return "Anagramas"
print(anagramas("Listen","Silent"))
