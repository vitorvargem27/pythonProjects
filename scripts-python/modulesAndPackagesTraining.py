from functionsUtilities import dado
from functionsUtilities import moeda

number = float(input('Write a number in R$ for consult the math situations : \n').strip())
value = float(input('Write a value in R$ for add in the original value :\n').strip())
choose = str(input('You want see a real coin?[Y]/[N]\n')).strip().upper()
boolean = ''

decisionCoin = moeda.decision(choose)
sumOfValues = dado.increase(number, value, boolean)
subtraction = dado.decrease(number, value, boolean)
double = dado.doubleValue(number, boolean)
halfNumber = dado.halfValue(number, boolean)

dado.resume(decisionCoin, number, value, sumOfValues, subtraction, double, halfNumber)


