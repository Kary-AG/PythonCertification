# Escenario
# Tu tarea es escribir un programa que:

#Le pregunta al usuario su cumpleaños (en el formato AAAAMMDD o AAAADMM o MMDDAAAA; en realidad, el orden de los dígitos no importa).
#Da como salida El Dígito de la Vida para la fecha ingresada.
def digitoDeVida(num):
    s1 = str(num)
    sum = 0
    if len(s1)==1:
        return s1
    for i in s1:
        sum+= int(i)
    return digitoDeVida(sum)

print(digitoDeVida(19991229))
