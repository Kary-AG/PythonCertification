#Escenario
#La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración,
#sin ejecutar las declaraciones dentro del ciclo.
#Se puede usar tanto con while y ciclos for.

#Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:

#Un ciclo for.
#El concepto de ejecución condicional (if-elif-else).
#La declaración continue.

#Tu programa debe:

#Pedir al usuario que ingrese una palabra.
palabra = input("Ingresa una palabra: ")
#Utiliza userWord = userWord.upper() para convertir la palabra ingresada
#por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena
#y el upper() muy pronto, no te preocupes.
palabra = palabra.upper()
#Utiliza la ejecución condicional y la instrucción continue para "comer" las siguientes vocales A , E , I , O , U de la palabra ingresada.
for i in range(len(palabra)):
    if (palabra[i] != "A") and (palabra[i] != "E") and (palabra[i]!= "I") and (palabra[i]!= "O") and (palabra[i]!= "U"):
        print(palabra[i])
        continue
#Imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada.
