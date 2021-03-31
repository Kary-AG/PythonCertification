#Escenario
#Tu tarea es escribir una función que verifique si un número es primo o no.
def isPrime(num):
    for n in range(2, num):
        if n == num: continue
        elif num % n == 0:
            return False
    return True

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()
