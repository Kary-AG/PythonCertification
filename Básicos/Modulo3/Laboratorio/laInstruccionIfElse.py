#ESCENARIO
#Érase una vez una tierra - una tierra de leche y miel,
#habitada por gente feliz y próspera. La gente pagaba impuestos,
#por supuesto, su felicidad tenía límites.
#El impuesto más importante, denominado Impuesto Personal de Ingresos
#(IPI, para abreviar) tenía que pagarse una vez al año y
#se evaluó utilizando la siguiente regla:
#Si el ingreso del ciudadano no era superior a 85,528 pesos,
#el impuesto era igual al 18% del ingreso menos 556 pesos y
#2 centavos (esta fue la llamada exención fiscal ).
#Si el ingreso era superior a esta cantidad, el impuesto
#era igual a 14,839 pesos y 2 centavos, más el 32% del
#excedente sobre 85,528 pesos.
#Tu tarea es escribir una calculadora de impuestos.

#Debe aceptar un valor de punto flotante: el ingreso.
#A continuación, debe imprimir el impuesto calculado, redondeado
#a pesos totales. Hay una función llamada round() que hará el
#redondeo por ti, la encontrarás en el código de esqueleto del editor

ingreso=float(input("Ingrese el ingreso anual:"))
if ingreso<=85528:
    impuesto = .18*ingreso-556.02
else:
    impuesto = 14839.02+(ingreso*.32)
impuesto=round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
