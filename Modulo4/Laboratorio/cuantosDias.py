#Escenario
#Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes)
#y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor
#year, tu función debería ser universal).

def isYearLeap(year):
    leap = False
    if(year%4 == 0) and (year%100 !=0):
        return True
    if (year % 100 == 0) and (year % 400 == 0) and (year %4 == 0):
        return True
    return leap

def daysInMonth(year, month):
    month31 = [1,3,5,7,8,10,12]
    if month==2:
        if isYearLeap: return 29
        else: return 28
    if month in month31: return 31
    else: return 30

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
