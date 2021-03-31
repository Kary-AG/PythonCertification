#Escenario
#Tu tarea es escribir y probar una función que toma tres argumentos
#(un año, un mes y un día del mes) y devuelve el día correspondiente del año,
#o devuelve None si cualquiera de los argumentos no es válido.
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

def dayOfYear(year, month, day):
    days =["sunday","monday","tuesday","wednesday", "thursday","friday","saturday"]
    if daysInMonth(year,month)>=day:
        return days[day%7]
    else:
        return
print(dayOfYear(2021, 3, 11))
