#ESCENARIO
#Tu tarea es escribir y probar una función que toma un argumento (un año)
#y devuelve True si el año es un año bisiesto, o False sí no lo es.
def isYearLeap(year):
    leap = False
    if(year%4 == 0) and (year%100 !=0):
        return True
    if (year % 100 == 0) and (year % 400 == 0) and (year %4 == 0):
        return True

    return leap

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
